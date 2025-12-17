from models.DAO import DAO
from models.bibliotecario import Bibliotecario


class BibliotecarioDAO(DAO):

    @classmethod
    def inserir(cls, b):
        conn = cls.conectar()
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO Bibliotecario (cpf, senha)
            VALUES (?, ?)
        """, (b.get_cpf(), b.get_senha()))

        conn.commit()
        conn.close()

    @classmethod
    def listar(cls):
        conn = cls.conectar()
        cur = conn.cursor()

        cur.execute("SELECT cpf, senha FROM Bibliotecario")
        rows = cur.fetchall()
        conn.close()

        return [Bibliotecario(*row) for row in rows]

    @classmethod
    def listar_id(cls, cpf):
        conn = cls.conectar()
        cur = conn.cursor()

        cur.execute("""
            SELECT cpf, senha FROM Bibliotecario
            WHERE cpf = ?
        """, (cpf,))

        row = cur.fetchone()
        conn.close()

        return Bibliotecario(*row) if row else None

    @classmethod
    def atualizar(cls, b):
        conn = cls.conectar()
        cur = conn.cursor()

        cur.execute("""
            UPDATE Bibliotecario
            SET senha = ?
            WHERE cpf = ?
        """, (b.get_senha(), b.get_cpf()))

        conn.commit()
        conn.close()

    @classmethod
    def excluir(cls, b):
        conn = cls.conectar()
        cur = conn.cursor()

        cur.execute("DELETE FROM Bibliotecario WHERE cpf = ?", (b.get_cpf(),))
        conn.commit()
        conn.close()
