from models.DAO import DAO
from models.exemplar import Exemplar


class ExemplarDAO(DAO):

    @classmethod
    def inserir(cls, e):
        conn = cls.conectar()
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO Exemplar (disponibilidade, codigo_livro)
            VALUES (?, ?)
        """, (e.get_disponibilidade(), e.get_codigo_livro()))

        e.set_id(cur.lastrowid)

        conn.commit()
        conn.close()

    @classmethod
    def listar(cls):
        conn = cls.conectar()
        cur = conn.cursor()

        cur.execute("""
            SELECT id, disponibilidade, codigo_livro
            FROM Exemplar
        """)

        rows = cur.fetchall()
        conn.close()

        return [Exemplar(*row) for row in rows]

    @classmethod
    def listar_id(cls, id):
        conn = cls.conectar()
        cur = conn.cursor()

        cur.execute("""
            SELECT id, disponibilidade, codigo_livro
            FROM Exemplar
            WHERE id = ?
        """, (id,))

        row = cur.fetchone()
        conn.close()

        return Exemplar(*row) if row else None

    @classmethod
    def atualizar(cls, e):
        conn = cls.conectar()
        cur = conn.cursor()

        cur.execute("""
            UPDATE Exemplar
            SET disponibilidade = ?, codigo_livro = ?
            WHERE id = ?
        """, (
            e.get_disponibilidade(),
            e.get_codigo_livro(),
            e.get_id()
        ))

        conn.commit()
        conn.close()

    @classmethod
    def excluir(cls, e):
        conn = cls.conectar()
        cur = conn.cursor()

        cur.execute("DELETE FROM Exemplar WHERE id = ?", (e.get_id(),))
        conn.commit()
        conn.close()
