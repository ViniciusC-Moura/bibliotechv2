from models.DAO import DAO
from models.multa import Multa


class MultaDAO(DAO):

    @classmethod
    def inserir(cls, m):
        conn = cls.conectar()
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO Multa (id_emprestimo, valor, descricao)
            VALUES (?, ?, ?)
        """, (
            m.get_id_emprestimo(),
            m.get_valor(),
            m.get_descricao()
        ))

        # sincroniza o id gerado pelo SQLite com o objeto
        m.set_id(cur.lastrowid)

        conn.commit()
        conn.close()

    @classmethod
    def listar(cls):
        conn = cls.conectar()
        cur = conn.cursor()

        cur.execute("""
            SELECT id, id_emprestimo, valor, descricao
            FROM Multa
        """)

        rows = cur.fetchall()
        conn.close()

        return [Multa(*row) for row in rows]

    @classmethod
    def listar_id(cls, id):
        conn = cls.conectar()
        cur = conn.cursor()

        cur.execute("""
            SELECT id, id_emprestimo, valor, descricao
            FROM Multa
            WHERE id = ?
        """, (id,))

        row = cur.fetchone()
        conn.close()

        return Multa(*row) if row else None

    @classmethod
    def atualizar(cls, m):
        conn = cls.conectar()
        cur = conn.cursor()

        cur.execute("""
            UPDATE Multa
            SET id_emprestimo = ?, valor = ?, descricao = ?
            WHERE id = ?
        """, (
            m.get_id_emprestimo(),
            m.get_valor(),
            m.get_descricao(),
            m.get_id()
        ))

        conn.commit()
        conn.close()

    @classmethod
    def excluir(cls, m):
        conn = cls.conectar()
        cur = conn.cursor()

        cur.execute("DELETE FROM Multa WHERE id = ?", (m.get_id(),))
        conn.commit()
        conn.close()
