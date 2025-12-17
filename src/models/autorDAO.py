from models.DAO import DAO
from models.autor import Autor


class AutorDAO(DAO):

    @classmethod
    def inserir(cls, a):
        conn = cls.conectar()
        cur = conn.cursor()

        cur.execute("INSERT INTO Autor (nome) VALUES (?)", (a.get_nome(),))
        a.set_id(cur.lastrowid)

        conn.commit()
        conn.close()

    @classmethod
    def listar(cls):
        conn = cls.conectar()
        cur = conn.cursor()

        cur.execute("SELECT id, nome FROM Autor")
        rows = cur.fetchall()
        conn.close()

        return [Autor(*row) for row in rows]

    @classmethod
    def listar_id(cls, id):
        conn = cls.conectar()
        cur = conn.cursor()

        cur.execute("SELECT id, nome FROM Autor WHERE id = ?", (id,))
        row = cur.fetchone()
        conn.close()

        return Autor(*row) if row else None

    @classmethod
    def atualizar(cls, a):
        conn = cls.conectar()
        cur = conn.cursor()

        cur.execute("""
            UPDATE Autor SET nome = ?
            WHERE id = ?
        """, (a.get_nome(), a.get_id()))

        conn.commit()
        conn.close()

    @classmethod
    def excluir(cls, a):
        conn = cls.conectar()
        cur = conn.cursor()

        cur.execute("DELETE FROM Autor WHERE id = ?", (a.get_id(),))
        conn.commit()
        conn.close()
