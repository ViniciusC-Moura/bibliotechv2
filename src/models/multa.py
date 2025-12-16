class Multa:
    def __init__(self, cpf_usuario, valor, descricao):
        self.set_cpf_usuario(cpf_usuario)
        self.set_valor(valor)
        self.set_descricao(descricao)
    
    def set_cpf_usuario(self, v):
        self.__cpf_usuario = v
    def set_valor(self, v):
        self.__valor = v
    def set_descricao(self, v)
        self.__descricao = v

    def get_cpf_usuario(self): return self.__cpf_usuario
    def get_valor(self): return self.__valor
    def get_descricao(self): return self.__descricao

    def __str__(self):
        return f"{self.__cpf_usuario} - {self.__valor} - {self.__descricao}"