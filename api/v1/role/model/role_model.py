#  Copyright (c) 2022. Hexagoon. Criador: Fabricio Gatto Lourençone. Todos os direitos reservados.
import datetime
from typing import Optional, Union, Any

from pydantic import BaseModel, Field


# Classe do tipo Usuario para fins de accountability
# sem importacao redundante
class UsuarioOutReduzido(BaseModel):
    id: Optional[Union[str, Any]] = Field(None, alias='_id')
    nome: str

    class Config:
        arbitrary_types_allowed = True


class RoleOut(BaseModel):
    id: Optional[Union[str, Any]] = Field(None, alias='_id')
    sigla: Optional[str]
    descricao: Optional[str]

    class SubRoles(BaseModel):
        sigla: Optional[str]

    sub_roles: Optional[list[SubRoles]] = []

    class Config:
        title = 'roles'
        arbitrary_types_allowed = True


class RoleOutDelete(BaseModel):
    id: Optional[Union[str, Any]] = Field(None, alias='_id')
    sigla: Optional[str]
    descricao: Optional[str]

    class UsuarioOutReduzido(BaseModel):
        id: Optional[Union[str, Any]] = Field(None, alias='_id')
        nome: str

    deletado_em: Optional[datetime.datetime]
    deletado_por: Optional[UsuarioOutReduzido]

    class SubRoles(BaseModel):
        sigla: Optional[str]

    sub_roles: Optional[list[SubRoles]] = []

    class Config:
        title = 'roles'
        arbitrary_types_allowed = True


class RoleInCreate(BaseModel):
    sigla: Optional[str]
    descricao: Optional[str]

    class Config:
        title = 'roles'
        arbitrary_types_allowed = True


class RoleInUpdate(BaseModel):
    id: Union[str, Any] = Field(None, alias='_id')
    sigla: Optional[str]
    descricao: Optional[str]

    class Config:
        title = 'roles'
        arbitrary_types_allowed = True


class RoleUsuarioOut(BaseModel):
    sigla: Optional[str]


class RoleUsuarioIn(BaseModel):
    id: Optional[Union[str, Any]] = Field(None, alias='_id')

    class Config:
        title = 'roles'
        arbitrary_types_allowed = True


class RoleUsuario(BaseModel):
    """ Role gerada para ser inserida como role no Usuario """
    id: Optional[Union[str, Any]] = Field(None, alias='_id')
    sigla: Optional[str]

    class Config:
        arbitrary_types_allowed = True


class SubRoles(BaseModel):
    """ Role gerada para ser inserida como sub_role em outra Role """
    id: Optional[Union[str, Any]] = Field(None, alias='_id')
    sigla: Optional[str]

    class Config:
        arbitrary_types_allowed = True


class Role(BaseModel):
    id: Optional[Union[str, Any]] = Field(None, alias='_id')
    sigla: Optional[str]
    descricao: Optional[str]

    sub_roles: Optional[list[SubRoles]] = []

    # accountability
    criado_em: Optional[datetime.datetime]
    criado_por: Optional[UsuarioOutReduzido]
    alterado_em: Optional[datetime.datetime]
    alterado_por: Optional[UsuarioOutReduzido]
    # soft_delete
    deletado_em: Optional[datetime.datetime]
    deletado_por: Optional[UsuarioOutReduzido]

    class Config:
        title = 'roles'
        arbitrary_types_allowed = True


class SubRoleIn(BaseModel):
    sub_role: str
    alterado_em: Optional[datetime.datetime]
    alterado_por: Optional[UsuarioOutReduzido]

    class Config:
        title = 'roles'
