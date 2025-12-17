from models.DAO import DAO
from models.autoria import Autoria


class AutoriaDAO(DAO):

    @classmethod
    def inserir(cls, a):
        conn = cls.conectar()
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO Autoria (id_autor, codigo_livro)
            VALUES (?, ?)
        """, (a.get_id_autor(), a.get_codigo_livro()))

        conn.commit()
        conn.close()

    @classmethod
    def listar(cls):
        conn = cls.conectar()
        cur = conn.cursor()

        cur.execute("SELECT id_autor, codigo_livro FROM Autoria")
        rows = cur.fetchall()
        conn.close()

        return [Autoria(*row) for row in rows]

    @classmethod
    def listar_id(cls, chave):
        id_autor, codigo_livro = chave
        conn = cls.conectar()
        cur = conn.cursor()

        cur.execute("""
            SELECT id_autor, codigo_livro
            FROM Autoria
            WHERE id_autor = ? AND codigo_livro = ?
        """, (id_autor, codigo_livro))

        row = cur.fetchone()
        conn.close()

        return Autoria(*row) if row else None

    @classmethod
    def atualizar(cls, a):
        pass  #tabela associativa

    @classmethod
    def excluir(cls, a):
        conn = cls.conectar()
        cur = conn.cursor()

        cur.execute("""
            DELETE FROM Autoria
            WHERE id_autor = ? AND codigo_livro = ?
        """, (a.get_id_autor(), a.get_codigo_livro()))

        conn.commit()
        conn.close()
