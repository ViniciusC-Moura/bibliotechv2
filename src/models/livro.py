class Livro:
    def __init__(self, codigo, nome):
        self.set_codigo(codigo)
        self.set_nome(nome)
    
    def set_codigo(self, v):
        self.__codigo = v
    def set_nome(self, v):
        self.__nome = v

    def get_codigo(self): return self.__codigo
    def get_nome(self): return self.__nome

    def __str__(self):
        return f"{self.__codigo} - {self.__nome}"