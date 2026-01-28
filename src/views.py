from models.usuario import Usuario
from models.usuarioDAO import UsuarioDAO

from models.bibliotecario import Bibliotecario
from models.bibliotecarioDAO import BibliotecarioDAO

from models.autor import Autor
from models.autorDAO import AutorDAO

from models.livro import Livro
from models.livroDAO import LivroDAO

from models.autoria import Autoria
from models.autoriaDAO import AutoriaDAO

from models.exemplar import Exemplar
from models.exemplarDAO import ExemplarDAO

from models.emprestimo import Emprestimo
from models.emprestimoDAO import EmprestimoDAO

from models.multa import Multa
from models.multaDAO import MultaDAO


class View:

    def criar_admin():
        for u in View.usuario_listar():
            if u.get_email() == "admin": return
        View.usuario_inserir("admin", "0", "admin", "admin", "admin", "1234")

    def bibliotecario_autenticar(cpf, senha):
        for b in View.bibliotecario_listar():
            if b.get_cpf() == cpf and b.get_senha() == senha:
                return {"cpf": b.get_cpf()}
        return None
    
    def usuario_autenticar(cpf, senha):
        for u in View.usuario_listar():
            if u.get_cpf() == cpf and u.get_senha() == senha:
                return {"cpf": u.get_cpf(), "nome": u.get_nome()}
        return None
    

    def bibliotecario_listar():
        return BibliotecarioDAO.listar()

    def bibliotecario_inserir(cpf, senha):
        if not cpf or not senha:
            raise ValueError("Nenhum valor pode ser nulo.")
        for b in View.bibliotecario_listar():
            if b.get_cpf() == cpf:
                raise ValueError("Bibliotecário já existe.")
        BibliotecarioDAO.inserir(Bibliotecario(cpf, senha))

    def bibliotecario_atualizar(cpf, senha):
        BibliotecarioDAO.atualizar(Bibliotecario(cpf, senha))

    def bibliotecario_excluir(cpf):
        UsuarioDAO.excluir(Usuario(cpf, "", "", "", "", ""))



    def usuario_listar():
        return UsuarioDAO.listar()

    def usuario_listar_cpf(cpf):
        return UsuarioDAO.listar_id(cpf)

    def usuario_inserir(cpf, matricula, nome, email, telefone, senha):
        if not cpf or not matricula or not nome or not email or not senha:
            raise ValueError("Nenhum valor pode ser nulo.")
        for u in View.usuario_listar():
            if u.get_cpf() == cpf:
                raise ValueError("Usuário já cadastrado.")
        UsuarioDAO.inserir(Usuario(cpf, matricula, nome, email, telefone, senha))

    def usuario_atualizar(cpf, matricula, nome, email, telefone, senha):
        UsuarioDAO.atualizar(Usuario(cpf, matricula, nome, email, telefone, senha))

    def usuario_excluir(cpf):
        for e in View.emprestimo_listar():
            if e.get_cpf_usuario() == cpf and e.get_dt_devolucao() is None:
                raise PermissionError("Usuário possui empréstimo ativo.")
        UsuarioDAO.excluir(Usuario(cpf, "", "", "", "", ""))



    def autor_listar():
        return AutorDAO.listar()

    def autor_listar_id(id):
        return AutorDAO.listar_id(id)

    def autor_inserir(nome):
        if not nome:
            raise ValueError("Nome não pode ser nulo.")
        AutorDAO.inserir(Autor(0, nome))

    def autor_atualizar(id, nome):
        AutorDAO.atualizar(Autor(id, nome))

    def autor_excluir(id):
        for a in View.autoria_listar():
            if a.get_id_autor() == id:
                raise PermissionError("Autor vinculado a livro.")
        AutorDAO.excluir(Autor(id, ""))



    def livro_listar():
        return LivroDAO.listar()

    def livro_listar_codigo(codigo):
        return LivroDAO.listar_id(codigo)

    def livro_inserir(nome):
        LivroDAO.inserir(Livro(0, nome))

    def livro_atualizar(codigo, nome):
        LivroDAO.atualizar(Livro(codigo, nome))

    def livro_excluir(codigo):
        for e in View.exemplar_listar():
            if e.get_codigo_livro() == codigo:
                raise PermissionError("Livro possui exemplares.")
        LivroDAO.excluir(Livro(codigo, ""))

    def livro_get_autores(codigo):
        ids_autores = [a.get_id_autor() for a in View.autoria_listar() if a.get_codigo_livro() == codigo]
        return [autor.get_nome() for autor in View.autor_listar() if autor.get_id() in ids_autores]

    def livro_get_exemplares(codigo):
        return [ex for ex in View.exemplar_listar() if ex.get_codigo_livro() == codigo]



    def autoria_listar():
        return AutoriaDAO.listar()

    def autoria_inserir(id_autor, codigo_livro):
        for a in View.autoria_listar():
            if a.get_id_autor() == id_autor and a.get_codigo_livro() == codigo_livro:
                raise ValueError("Autoria já cadastrada.")
        AutoriaDAO.inserir(Autoria(id_autor, codigo_livro))

    def autoria_excluir(id_autor, codigo_livro):
        AutoriaDAO.excluir(Autoria(id_autor, codigo_livro))



    def exemplar_listar():
        return ExemplarDAO.listar()

    def exemplar_listar_id(id):
        return ExemplarDAO.listar_id(id)

    def exemplar_inserir(codigo_livro):
        ExemplarDAO.inserir(Exemplar(0, True, codigo_livro))

    def exemplar_atualizar(id, disponibilidade, codigo_livro):
        ExemplarDAO.atualizar(Exemplar(id, disponibilidade, codigo_livro))

    def exemplar_excluir(id):
        for e in View.emprestimo_listar():
            if e.get_id_exemplar() == id and e.get_dt_devolucao() is None:
                raise PermissionError("Exemplar emprestado.")
        ExemplarDAO.excluir(Exemplar(id, False, 0))



    def emprestimo_listar():
        return EmprestimoDAO.listar()

    def emprestimo_inserir(dt_emprestimo, dt_prazo, cpf_usuario, id_exemplar, confirmado):
        e = Emprestimo(0, dt_emprestimo, dt_prazo, None, cpf_usuario, id_exemplar, confirmado)
        EmprestimoDAO.inserir(e)

    def emprestimo_excluir(id):
        EmprestimoDAO.excluir(Emprestimo(id, "", "", None, "", 0, False))
        for m in View.multa_listar():
            if m.get_id_emprestimo() == id: MultaDAO.excluir(m)

    def emprestimo_atualizar(id, dt_emprestimo, dt_prazo, dt_devolucao, cpf_usuario, id_exemplar, confirmado):
        EmprestimoDAO.atualizar(Emprestimo(id, dt_emprestimo, dt_prazo, dt_devolucao, cpf_usuario, id_exemplar, confirmado))

    def emprestimo_devolver(id, dt_devolucao):
        e = EmprestimoDAO.listar_id(id)
        e.set_dt_devolucao(dt_devolucao)
        EmprestimoDAO.atualizar(e)
        ex = View.exemplar_listar_id(e.get_id_exemplar())
        ex.set_disponibilidade(True)
        ExemplarDAO.atualizar(ex)



    def multa_listar():
        return MultaDAO.listar()

    def multa_inserir(id_emprestimo, valor, descricao):
        MultaDAO.inserir(Multa(0, id_emprestimo, valor, descricao))

    def multa_excluir(id):
        MultaDAO.excluir(Multa(id, 0, 0, ""))
