from models.DAO import DAO
from models.usuario import Usuario


class UsuarioDAO(DAO):

    @classmethod
    def inserir(cls, u):
        conn = cls.conectar()
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO Usuario (cpf, matricula, nome, telefone, email, senha)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            u.get_cpf(),
            u.get_matricula(),
            u.get_nome(),
            u.get_telefone(),
            u.get_email(),
            u.get_senha()
        ))

        conn.commit()
        conn.close()

    @classmethod
    def listar(cls):
        conn = cls.conectar()
        cur = conn.cursor()

        cur.execute("""
            SELECT cpf, matricula, nome, telefone, email, senha
            FROM Usuario
        """)

        rows = cur.fetchall()
        conn.close()

        return [Usuario(*row) for row in rows]

    @classmethod
    def listar_id(cls, cpf):
        conn = cls.conectar()
        cur = conn.cursor()

        cur.execute("""
            SELECT cpf, matricula, nome, telefone, email, senha
            FROM Usuario
            WHERE cpf = ?
        """, (cpf,))

        row = cur.fetchone()
        conn.close()

        return Usuario(*row) if row else None

    @classmethod
    def atualizar(cls, u):
        conn = cls.conectar()
        cur = conn.cursor()

        cur.execute("""
            UPDATE Usuario
            SET matricula = ?, nome = ?, telefone = ?, email = ?, senha = ?
            WHERE cpf = ?
        """, (
            u.get_matricula(),
            u.get_nome(),
            u.get_telefone(),
            u.get_email(),
            u.get_senha(),
            u.get_cpf()
        ))

        conn.commit()
        conn.close()

    @classmethod
    def excluir(cls, u):
        conn = cls.conectar()
        cur = conn.cursor()

        cur.execute("DELETE FROM Usuario WHERE cpf = ?", (u.get_cpf(),))
        conn.commit()
        conn.close()
