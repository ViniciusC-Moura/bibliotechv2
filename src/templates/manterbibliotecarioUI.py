import streamlit as st
import pandas as pd
import time
from views import View

class ManterBibliotecarioUI:

    def main():
        st.header("Cadastro de Bibliotecários")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterBibliotecarioUI.listar()
        with tab2: ManterBibliotecarioUI.inserir()
        with tab3: ManterBibliotecarioUI.atualizar()
        with tab4: ManterBibliotecarioUI.excluir()

    def listar():
        biblios = View.bibliotecario_listar()
        if len(biblios) == 0:
            st.write("Nenhum bibliotecário cadastrado")
        else:
            dados = [{"CPF": b.get_cpf()} for b in biblios]
            st.dataframe(pd.DataFrame(dados), use_container_width=True)

    def inserir():
        cpf = st.text_input("CPF")
        senha = st.text_input("Senha")
        if st.button("Inserir"):
            View.bibliotecario_inserir(cpf, senha)
            st.success("Bibliotecário cadastrado com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        st.info("Atualização não prevista para bibliotecário")

    def excluir():
        biblios = View.bibliotecario_listar()
        if len(biblios) == 0:
            st.write("Nenhum bibliotecário cadastrado")
        else:
            op = st.selectbox("Bibliotecário a ser excluído", biblios)
            if st.button("Excluir"):
                View.bibliotecario_excluir.excluir(op)
                st.success("Bibliotecário excluído")
                time.sleep(2)
                st.rerun()
