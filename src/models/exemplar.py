class Exemplar:
    def __init__(self, id, disponibilidade, codigo_livro):
        self.set_id(id)
        self.set_disponibilidade(disponibilidade)
        self.set_codigo_livro(codigo_livro)
    
    def set_id(self, v):
        self.__id = v
    def set_disponibilidade(self, v):
        self.__disponibilidade = v
    def set_codigo_livro(self, v):
        self.__codigo_livro = v

    def get_id(self): return self.__id
    def get_disponibilidade(self): return self.__disponibilidade
    def get_codigo_livro(self): return self.__codigo_livro

    def __str__(self):
        return f"{self.__id} - {self.__disponibilidade} - Livro: {self.__codigo_livro}"