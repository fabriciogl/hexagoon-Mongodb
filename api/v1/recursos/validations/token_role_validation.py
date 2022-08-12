#  Copyright (c) 2021. Hexagoon. Criador: Fabricio Gatto Lourençone. Todos os direitos reservados.
from typing import Tuple, Optional, Any

import jwt
from fastapi.params import Depends
from fastapi.security import SecurityScopes
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session
from starlette.requests import Request

from api.v1.recursos.basic_exceptions.token_exceptions import TokenException, \
    RoleException
from api.v1.recursos.response_handler import ResponseHandler
from api.v1.usuario.excecoes.usuario_excecoes import UsuarioFindException
from api.v1.usuario.model.usuario_model import Usuario, UsuarioTokenOut
from banco_dados.mongodb.configuracao.MongoConection import Operacoes
from config import settings


def valida_token(
        request: Request,
        token: Optional[str] = None
) -> Tuple[UsuarioTokenOut, Any, Request]:
    # inicia um objeto de conexão com o banco
    operacao = Operacoes()
    # verifica se existe token no header
    # e depois se token foi enviado por parametro na url
    # por fim levanta erro de ausência de token
    if request.headers.get('Authorization'):
        token = request.headers.get('Authorization').replace('Bearer ', '')
    elif token := token:
        pass
    else:
        raise TokenException(ordem=1, request=request)

    try:
        payload = jwt.decode(
            jwt=token,
            key=settings.jwt_hash,
            algorithms=[settings.jwt_algo]
        )
        _id: str = payload.get('sub')
        ip: str = payload.get('on')

    except jwt.ExpiredSignatureError:
        raise TokenException(ordem=2, request=request)
    except (jwt.DecodeError, jwt.InvalidAlgorithmError, jwt.InvalidSignatureError):
        raise TokenException(ordem=3, request=request)

    # Verifica se o IP do request é o mesmo do Token
    if ip != request.client.host:
        raise TokenException(ordem=4, request=request)

    # busca o usuário no banco de dados
    try:
        usuario_data: UsuarioTokenOut = UsuarioTokenOut(**operacao.find_lef_join(id=_id, collection='usuarios'))

    except NoResultFound:
        raise UsuarioFindException(ordem=1, _id=_id, request=request)

    return usuario_data, operacao, request


async def valida_role(
        security_scopes: SecurityScopes,
        usuario_session_request: Tuple[UsuarioTokenOut, Operacoes, Request] = Depends(valida_token)
) -> ResponseHandler:
    usuario, operacao, request = usuario_session_request

    can_access = False
    # roles originais
    roles_siglas = [role['sigla'] for role in usuario.rolePrecedencias]
    precedencias = []
    for role in usuario.rolePrecedencias:
        precedencias.extend(role['precedencias'])
    precedencias_sigla = [precedencia['sigla'] for precedencia in precedencias]
    # sub_roles
    # roles = [role for role in usuario.roles]
    # a_sub_roles = [a_sub_roles for role in roles for a_sub_roles in role.a_sub_roles]
    # all_sub_roles = [a.sub_role.sigla for a in a_sub_roles]
    # todas as roles
    all_roles = set(roles_siglas + precedencias_sigla)
    # verifica as roles necessárias para o endpoint
    for role in security_scopes.scopes:
        if role in all_roles:
            can_access = True
            break

    if not can_access:
        raise RoleException(usuario=usuario, request=request)

    handler = ResponseHandler(operacao=operacao)
    handler.usuario = usuario
    handler.request = request

    # adiciona o handler ao request para ser monitorado ao final da requisicao
    request.state._state['handler'] = handler

    # adiciona o handler à conexão para poder ser utilizado pelos listener do SQLAlchemy
    # SEGURO SOMENTE PARA ARQUITETURA SÍNCRONA (TESTAR NO CASO DE ARQUITETURA ASSÍCRONA)
    # PARA SABER SE UMA CONEXÃO É REAPROVEITADA ENTRE VÁRIAS SESSÕES
    # operacao.bind.connection.info['handler'] = handler

    # Dependencies com yield permitem incluir um finally que é executado após a resposta
    # ao usuário.
    try:
        yield handler
    finally:
        del handler
