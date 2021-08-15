#  Copyright (c) 2021. QuickTest app escrito por Fabricio Gatto Lourençone. Todos os direitos reservados.
from pydantic import BaseModel
from starlette.exceptions import HTTPException


class MongoFindException1(HTTPException):
    """Exceção a ser utilizada quando ocorre erro na busca de objeto"""

    def __init__(self, model_name: str, i: str):
        """

        Args:
            model_name: string do nome do objeto
            i:  identificação do objeto
        """
        super().__init__(404, f'{model_name} sob id {i} não encontrado.')

class MongoFindException2(HTTPException):
    """Exceção a ser utilizada quando ocorre erro na busca de objeto"""

    def __init__(self):
        """

        Args:
            model_name: string do nome do objeto
            i:  identificação do objeto
        """
        super().__init__(404, f'Busca sem resultado.')


class MongoCreateException(HTTPException):
    """Exceção a ser utilizada quando ocorre erro na criação de objeto"""

    def __init__(self, objeto: BaseModel):
        """

        Args:
            objeto: "Model sob acao"
        """
        super().__init__(422, f'{type(objeto).__name__} sob id {objeto.id} não foi criado.')

class MongoUpsertedException(HTTPException):
    """Exceção a ser utilizada quando ocorre upsert na criação de objeto"""

    def __init__(self, objeto: BaseModel):
        """

        Args:
            objeto: "Model sob acao"
        """
        super().__init__(422, f'{type(objeto).__name__} sob id {objeto.id} já existe.')

class MongoUpdateException(HTTPException):
    pass

class MongoOperationException(HTTPException):
    """Exceção a ser utilizada quando ocorre erro na conexão com o banco"""

    def __init__(self):
        super().__init__(422, f'Falha temporária na conexão com o Banco.')
