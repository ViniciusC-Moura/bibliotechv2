import sqlite3

class Database:
    DB_NAME = "banco.db"

    @classmethod
    def conectar(cls):
        return sqlite3.connect(cls.DB_NAME)

    @classmethod
    def criar_tabelas(cls):
        conn = cls.conectar()
        cursor = conn.cursor()

        #habilita chaves estrangeiras no sqlite
        cursor.execute("PRAGMA foreign_keys = ON;")

        cursor.executescript("""
            CREATE TABLE IF NOT EXISTS Bibliotecario (
                cpf TEXT PRIMARY KEY,
                senha TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS Usuario (
                cpf TEXT PRIMARY KEY,
                matricula TEXT UNIQUE NOT NULL,
                nome TEXT NOT NULL,
                telefone TEXT NOT NULL,
                email TEXT NOT NULL,
                senha TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS Autor (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS Livro (
                codigo INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS Autoria (
                id_autor INTEGER NOT NULL,
                codigo_livro INTEGER NOT NULL,
                PRIMARY KEY (id_autor, codigo_livro),
                FOREIGN KEY (id_autor) REFERENCES Autor(id),
                FOREIGN KEY (codigo_livro) REFERENCES Livro(codigo)
            );

            CREATE TABLE IF NOT EXISTS Exemplar (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                disponibilidade INTEGER NOT NULL,
                codigo_livro INTEGER NOT NULL,
                FOREIGN KEY (codigo_livro) REFERENCES Livro(codigo)
            );

            CREATE TABLE IF NOT EXISTS Emprestimo (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                dt_emprestimo TEXT NOT NULL,
                dt_prazo TEXT NOT NULL,
                dt_devolucao TEXT,
                cpf_usuario TEXT NOT NULL,
                id_exemplar INTEGER NOT NULL,
                FOREIGN KEY (cpf_usuario) REFERENCES Usuario(cpf),
                FOREIGN KEY (id_exemplar) REFERENCES Exemplar(id)
            );
                             
            CREATE TABLE IF NOT EXISTS Multa (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cpf_usuario TEXT NOT NULL,
                valor REAL NOT NULL,
                descricao TEXT NOT NULL,
                FOREIGN KEY (cpf_usuario) REFERENCES Usuario(cpf)
            );
        """)

        conn.commit()
        conn.close()
