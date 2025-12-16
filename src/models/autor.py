class Autor:
    def __init__(self, id, nome):
        self.set_id(id)
        self.set_nome(nome)
    
    def set_id(self, v):
        self.__id = v
    def set_nome(self, v):
        self.__nome = v

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome

    def __str__(self):
        return f"{self.__id} - {self.__nome}"