import streamlit as st
import pandas as pd
import time
from views import View

class ManterAutorUI:

    def main():
        st.header("Cadastro de Autores")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterAutorUI.listar()
        with tab2: ManterAutorUI.inserir()
        with tab3: ManterAutorUI.atualizar()
        with tab4: ManterAutorUI.excluir()

    def listar():
        autores = View.autor_listar()
        if len(autores) == 0:
            st.write("Nenhum autor cadastrado")
        else:
            dados = [{"ID": a.get_id(), "Nome": a.get_nome()} for a in autores]
            st.dataframe(pd.DataFrame(dados), use_container_width=True)

    def inserir():
        nome = st.text_input("Nome do autor")
        if st.button("Inserir"):
            View.autor_inserir(nome)
            st.success("Autor cadastrado com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        autores = View.autor_listar()
        if len(autores) == 0:
            st.write("Nenhum autor cadastrado")
        else:
            op = st.selectbox("Autor", autores)
            nome = st.text_input("Novo nome", op.get_nome())
            if st.button("Atualizar"):
                View.autor_atualizar(op.get_id(), nome)
                st.success("Autor atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        autores = View.autor_listar()
        if len(autores) == 0:
            st.write("Nenhum autor cadastrado")
        else:
            op = st.selectbox("Autor a ser excluído", autores)
            if st.button("Excluir"):
                View.autor_excluir(op.get_id())
                st.success("Autor excluído com sucesso")
                time.sleep(2)
                st.rerun()
