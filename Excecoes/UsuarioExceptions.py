#  Copyright (c) 2021. QuickTest app escrito por Fabricio Gatto Lourençone. Todos os direitos reservados.
from starlette.exceptions import HTTPException
from Model.Usuario import Usuario


class UsuarioCreateException(HTTPException):
    """Exceção a ser utilizada quando ocorre erro na criacao de model"""

    def __init__(self, model: Usuario, msg: str):
        """

        Args:
            model_name: string do nome do model
            i:  identificação do model
        """
        print(msg)
        super().__init__(422, f'O {type(model).__name__} com email {model.email} não foi criado.')


class UsuarioUpdateException(HTTPException):
    """Exceção a ser utilizada quando ocorre erro no update do model"""

    def __init__(self, model: Usuario):
        """

        Args:
            model_name: string do nome do model
            i:  identificação do model
        """
        super().__init__(422, f'O campo email do {type(model).__name__} não pode ser alterado.')
