class Bibliotecario:
    def __init__(self, cpf, senha):
        self.set_cpf(cpf)
        self.set_senha(senha)
    
    def set_cpf(self, v):
        self.__cpf = v
    def set_senha(self, v):
        self.__senha = v

    def get_cpf(self): return self.__cpf
    def get_senha(self): return self.__senha

    def __str__(self):
        return f"Bibliotecário - CPF: {self.__cpf}"