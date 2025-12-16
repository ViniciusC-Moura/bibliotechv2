class Usuario:
    def __init__(self, cpf, matricula, nome, telefone, email, senha):
        self.set_cpf(cpf)
        self.set_matricula(matricula)
        self.set_nome(nome)
        self.set_telefone(telefone)
        self.set_email(email)
        self.set_senha(senha)

    def set_cpf(self, v): 
        self.__cpf = v
    def set_matricula(self, v): 
        self.__matricula = v
    def set_nome(self, v): 
        self.__nome = v
    def set_telefone(self, v): 
        self.__telefone = v
    def set_email(self, v):
        self.__email = v
    def set_senha(self, v):
        self.__senha = v

    def get_cpf(self): return self.__cpf
    def get_matricula(self): return self.__matricula
    def get_nome(self): return self.__nome
    def get_telefone(self): return self.__telefone
    def get_email(self): return self.__email
    def get_senha(self): return self.__senha

    def __str__(self):
        return f"{self.__nome} - {self.__cpf} - {self.__email}"