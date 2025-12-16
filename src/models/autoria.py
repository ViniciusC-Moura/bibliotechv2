class Autoria:
    def __init__(self, id_autor, codigo_livro):
        self.set_id_autor(id)
        self.set_codigo_livro(codigo_livro)
    
    def set_id_autor(self, v):
        self.__id_autor = v
    def set_codigo_livro(self, v):
        self.__codigo_livro = v

    def get_id_autor(self): return self.__id_autor
    def get_codigo_livro(self): return self.__codigo_livro

    def __str__(self):
        return f"Autor: {self.__id_autor} - Livro: {self.__codigo_livro}"