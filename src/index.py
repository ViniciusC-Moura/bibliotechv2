from templates.manterlivroUI import ManterLivroUI

from templates.loginUI import LoginUI
from views import View
import streamlit as st

class IndexUI:

    def menu_visitante():
        op = st.sidebar.selectbox("Menu", ["Entrar no Sistema"])
        if op == "Entrar no Sistema": LoginUI.main()

    def menu_usuario():
        op = st.sidebar.selectbox("Menu", ["Verificar disponibilidade de livros", "Reservar livro"])
        if op == "Verificar disponibilidade de livros": DisponibilidadeLivrosUI.main()
        if op == "Reservar livro": ReservarLivroUI.main()


    def menu_bibliotecario():
        op = st.sidebar.selectbox(
            "Menu",
            [
                "Cadastrar livro",
                "Realizar empréstimo",
                "Registrar devolução",
                "Renovar empréstimo",
                "Consultar histórico",
                "Emitir multa"
            ]
        )
        if op == "Cadastrar livro":
            ManterLivroUI.main()
        if op == "Realizar empréstimo":
            RealizarEmprestimoUI.main()
        if op == "Registrar devolução":
            RegistrarDevolucaoUI.main()
        if op == "Renovar empréstimo":
            RenovarEmprestimoUI.main()
        if op == "Consultar histórico":
            ConsultarHistoricoUI.main()
        if op == "Emitir multa":
            EmitirMultaUI.main()

    def menu_admin():
        op = st.sidebar.selectbox(
            "Menu",
            [
                "Cadastro de usuários",
                "Cadastro de bibliotecários",
                "Cadastro de autores",
                "Cadastro de livros",
                "Cadastro de exemplares",
                "Cadastro de empréstimos",
                "Cadastro de multas",
            ]
        )

        if op == "Cadastro de usuários":
            ManterUsuarioUI.main()
        if op == "Cadastro de bibliotecários":
            ManterBibliotecarioUI.main()
        if op == "Cadastro de autores":
            ManterAutorUI.main()
        if op == "Cadastro de livros":
            ManterLivroUI.main()
        if op == "Cadastro de exemplares":
            ManterExemplarUI.main()
        if op == "Cadastro de empréstimos":
            ManterEmprestimoUI.main()
        if op == "Cadastro de multas":
            ManterMultaUI.main()

    def sidebar():
        if "client_cpf" not in st.session_state: IndexUI.menu_visitante()
        else:
            admin = st.session_state["client_nome"] == "admin"
            st.sidebar.write("Bem-vindo(a), " + st.session_state["client_nome"])
            if admin: IndexUI.menu_admin()
            if st.session_state["client_nivel"] == "usuario" and not admin: IndexUI.menu_usuario()
            if st.session_state["client_nivel"] == "bibliotecario": IndexUI.menu_bibliotecario()
            IndexUI.sair_do_sistema()

    def main():
        View.criar_admin()
        IndexUI.sidebar()

    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            del st.session_state["client_cpf"]
            del st.session_state["client_nome"]
            del st.session_state["client_nivel"]
            st.rerun()

IndexUI.main()