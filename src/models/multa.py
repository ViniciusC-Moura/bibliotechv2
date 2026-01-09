class Multa:
    def __init__(self, id, id_emprestimo, valor, descricao):
        self.set_id(id)
        self.set_id_emprestimo(id_emprestimo)
        self.set_valor(valor)
        self.set_descricao(descricao)
    
    def set_id(self, v):
        self.__id = v
    def set_id_emprestimo(self, v):
        self.__id_emprestimo = v
    def set_valor(self, v):
        self.__valor = v
    def set_descricao(self, v):
        self.__descricao = v

    def get_id(self): return self.__id
    def get_id_emprestimo(self): return self.__id_emprestimo
    def get_valor(self): return self.__valor
    def get_descricao(self): return self.__descricao

    def __str__(self):
        return f"{self.__id} - {self.__id_emprestimo} - {self.__valor} - {self.__descricao}"