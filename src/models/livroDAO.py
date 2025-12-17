from models.DAO import DAO
from models.livro import Livro


class LivroDAO(DAO):

    @classmethod
    def inserir(cls, l):
        conn = cls.conectar()
        cur = conn.cursor()

        cur.execute("INSERT INTO Livro (nome) VALUES (?)", (l.get_nome(),))
        l.set_codigo(cur.lastrowid)

        conn.commit()
        conn.close()

    @classmethod
    def listar(cls):
        conn = cls.conectar()
        cur = conn.cursor()

        cur.execute("SELECT codigo, nome FROM Livro")
        rows = cur.fetchall()
        conn.close()

        return [Livro(*row) for row in rows]

    @classmethod
    def listar_id(cls, codigo):
        conn = cls.conectar()
        cur = conn.cursor()

        cur.execute("""
            SELECT codigo, nome FROM Livro
            WHERE codigo = ?
        """, (codigo,))

        row = cur.fetchone()
        conn.close()

        return Livro(*row) if row else None

    @classmethod
    def atualizar(cls, l):
        conn = cls.conectar()
        cur = conn.cursor()

        cur.execute("""
            UPDATE Livro SET nome = ?
            WHERE codigo = ?
        """, (l.get_nome(), l.get_codigo()))

        conn.commit()
        conn.close()

    @classmethod
    def excluir(cls, l):
        conn = cls.conectar()
        cur = conn.cursor()

        cur.execute("DELETE FROM Livro WHERE codigo = ?", (l.get_codigo(),))
        conn.commit()
        conn.close()
