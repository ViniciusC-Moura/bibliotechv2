import streamlit as st
import pandas as pd
import time
from views import View

class ManterUsuarioUI:

    def main():
        st.header("Cadastro de Usuários")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterUsuarioUI.listar()
        with tab2: ManterUsuarioUI.inserir()
        with tab3: ManterUsuarioUI.atualizar()
        with tab4: ManterUsuarioUI.excluir()

    def listar():
        usuarios = View.usuario_listar()
        if len(usuarios) == 0:
            st.write("Nenhum usuário cadastrado")
        else:
            dados = []
            for u in usuarios:
                dados.append({
                    "CPF": u.get_cpf(),
                    "Nome": u.get_nome(),
                    "Email": u.get_email()
                })
            st.dataframe(pd.DataFrame(dados), use_container_width=True)

    def inserir():
        cpf = st.text_input("CPF")
        matricula = st.text_input("Matrícula")
        nome = st.text_input("Nome")
        email = st.text_input("Email")
        telefone = st.text_input("Telefone")
        senha = st.text_input("Senha")

        if st.button("Inserir"):
            View.usuario_inserir(cpf, matricula, nome, email, telefone, senha)
            st.success("Usuário cadastrado com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        usuarios = View.usuario_listar()
        if len(usuarios) == 0:
            st.write("Nenhum usuário cadastrado")
        else:
            op = st.selectbox("Usuário", usuarios)
            nome = st.text_input("Nome", op.get_nome())
            email = st.text_input("Email", op.get_email())
            telefone = st.text_input("Telefone", op.get_telefone())
            senha = st.text_input("Senha", op.get_senha())

            if st.button("Atualizar"):
                View.usuario_atualizar(op.get_cpf(), op.get_matricula(), nome, email, telefone, senha)
                st.success("Usuário atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        usuarios = View.usuario_listar()
        if len(usuarios) == 0:
            st.write("Nenhum usuário cadastrado")
        else:
            op = st.selectbox("Usuário a ser excluido", usuarios)
            if st.button("Excluir"):
                View.usuario_excluir(op.get_cpf())
                st.success("Usuário excluído com sucesso")
                time.sleep(2)
                st.rerun()
