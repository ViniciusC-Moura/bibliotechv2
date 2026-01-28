class Emprestimo:
    def __init__(self, id, dt_emprestimo, dt_prazo, dt_devolucao, cpf_usuario, id_exemplar, confirmado):
        self.set_id(id)
        self.set_dt_emprestimo(dt_emprestimo)
        self.set_dt_prazo(dt_prazo)
        self.set_dt_devolucao(dt_devolucao)        
        self.set_cpf_usuario(cpf_usuario)
        self.set_id_exemplar(id_exemplar)
        self.set_confirmado(confirmado)

    def set_id(self, v):
        self.__id = v
    def set_dt_emprestimo(self, v): 
        self.__dt_emprestimo = v
    def set_cpf_usuario(self, v): 
        self.__cpf_usuario = v
    def set_id_exemplar(self, v): 
        self.__id_exemplar = v
    def set_dt_prazo(self, v): 
        self.__dt_prazo = v
    def set_dt_devolucao(self, v):
        self.__dt_devolucao = v
    def set_confirmado(self, v):
        self.__confirmado = v

    def get_id(self): return self.__id
    def get_dt_emprestimo(self): return self.__dt_emprestimo
    def get_cpf_usuario(self): return self.__cpf_usuario
    def get_id_exemplar(self): return self.__id_exemplar
    def get_dt_prazo(self): return self.__dt_prazo
    def get_dt_devolucao(self): return self.__dt_devolucao
    def get_confirmado(self): return self.__confirmado

    def __str__(self):
        return f"{self.__id} - {self.__cpf_usuario} - {self.__id_exemplar} - {self.__dt_devolucao}"