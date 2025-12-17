from models.DAO import DAO
from models.emprestimo import Emprestimo


class EmprestimoDAO(DAO):

    @classmethod
    def inserir(cls, e):
        conn = cls.conectar()
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO Emprestimo
            (dt_emprestimo, dt_prazo, dt_devolucao, cpf_usuario, id_exemplar)
            VALUES (?, ?, ?, ?, ?)
        """, (
            e.get_dt_emprestimo(),
            e.get_dt_prazo(),
            e.get_dt_devolucao(),
            e.get_cpf_usuario(),
            e.get_id_exemplar()
        ))

        e.set_id(cur.lastrowid)

        conn.commit()
        conn.close()

    @classmethod
    def listar(cls):
        conn = cls.conectar()
        cur = conn.cursor()

        cur.execute("""
            SELECT id, dt_emprestimo, dt_prazo, dt_devolucao, cpf_usuario, id_exemplar
            FROM Emprestimo
        """)

        rows = cur.fetchall()
        conn.close()

        return [Emprestimo(*row) for row in rows]

    @classmethod
    def listar_id(cls, id):
        conn = cls.conectar()
        cur = conn.cursor()

        cur.execute("""
            SELECT id, dt_emprestimo, dt_prazo, dt_devolucao, cpf_usuario, id_exemplar
            FROM Emprestimo
            WHERE id = ?
        """, (id,))

        row = cur.fetchone()
        conn.close()

        return Emprestimo(*row) if row else None

    @classmethod
    def atualizar(cls, e):
        conn = cls.conectar()
        cur = conn.cursor()

        cur.execute("""
            UPDATE Emprestimo
            SET dt_emprestimo = ?, dt_prazo = ?, dt_devolucao = ?,
                cpf_usuario = ?, id_exemplar = ?
            WHERE id = ?
        """, (
            e.get_dt_emprestimo(),
            e.get_dt_prazo(),
            e.get_dt_devolucao(),
            e.get_cpf_usuario(),
            e.get_id_exemplar(),
            e.get_id()
        ))

        conn.commit()
        conn.close()

    @classmethod
    def excluir(cls, e):
        conn = cls.conectar()
        cur = conn.cursor()

        cur.execute("DELETE FROM Emprestimo WHERE id = ?", (e.get_id(),))
        conn.commit()
        conn.close()
