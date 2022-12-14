#  Copyright (c) 2022. Hexagoon. Criador: Fabricio Gatto Lourençone. Todos os direitos reservados.

from recursos.basic_exceptions.mongo_exceptions import MongoFindException
from recursos.regras_initiallizer import RegrasInitiallizer
from api.v1.role.model.role_model import Role


class RoleRegras(RegrasInitiallizer):

    def regra_1(self):
        """
        use : [find-1, inactivate-1, update-1, soft_delete-1, adiciona_sub_role-1, remove_sub_role-1]

        verifica se o id existe e se está ativo
        """
        try:
            self.data: Role = Role(
                **self.handler.operacao.find_one(id=self._id, collection='roles')
            )
        except TypeError:
            raise MongoFindException(self._id, 'Role')
