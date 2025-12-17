from models.autor import Autor
from models.autorDAO import AutorDAO
from database import Database

def main():
    print("INICIALIZANDO BANCO")
    Database.criar_tabelas()

    print("TESTE DE PERSISTÊNCIA (Autor)")

    autor = Autor(None, "Machado de Assis")

    AutorDAO.inserir(autor)

    print("Autor salvo no banco:")
    print(autor)

    autor_lido = AutorDAO.listar_id(autor.get_id())

    print("\nAutor lido do banco:")
    print(autor_lido)

main()