from abc import ABC, abstractmethod

class DAO(ABC):
    _objetos = []
    @classmethod
    def inserir(cls, obj):
        pass

    @classmethod
    def listar(cls):
        pass

    @classmethod
    def listar_id(cls, id):
        pass

    @classmethod
    def atualizar(cls, obj):
        pass

    @classmethod
    def excluir(cls, obj):
        pass

    @classmethod
    @abstractmethod
    def abrir(cls):
        pass

    @classmethod
    @abstractmethod
    def salvar(cls):
        pass