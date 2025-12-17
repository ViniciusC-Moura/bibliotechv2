import sqlite3
from abc import ABC, abstractmethod

class DAO(ABC):
    DB_NAME = "banco.db"

    @classmethod
    def conectar(cls):
        conn = sqlite3.connect(cls.DB_NAME)
        conn.execute("PRAGMA foreign_keys = ON;")
        return conn

    @classmethod
    @abstractmethod
    def inserir(cls, obj):
        pass

    @classmethod
    @abstractmethod
    def listar(cls):
        pass

    @classmethod
    @abstractmethod
    def listar_id(cls, id):
        pass

    @classmethod
    @abstractmethod
    def atualizar(cls, obj):
        pass

    @classmethod
    @abstractmethod
    def excluir(cls, obj):
        pass
