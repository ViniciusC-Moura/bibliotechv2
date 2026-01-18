import streamlit as st
import pandas as pd
import time
from views import View

class ManterExemplarUI:

    def main():
        st.header("Cadastro de Exemplares")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterExemplarUI.listar()
        with tab2: ManterExemplarUI.inserir()
        with tab3: ManterExemplarUI.atualizar()
        with tab4: ManterExemplarUI.excluir()

    def listar():
        exs = View.exemplar_listar()
        if len(exs) == 0:
            st.write("Nenhum exemplar cadastrado")
        else:
            dados = []
            for e in exs:
                dados.append({
                    "ID": e.get_id(),
                    "Disponível": e.get_disponibilidade(),
                    "Livro": e.get_codigo_livro()
                })
            st.dataframe(pd.DataFrame(dados), use_container_width=True)

    def inserir():
        codigo = st.text_input("Código do livro")
        if st.button("Inserir"):
            View.exemplar_inserir(codigo)
            st.success("Exemplar cadastrado")
            time.sleep(2)
            st.rerun()

    def atualizar():
        exs = View.exemplar_listar()
        if len(exs) == 0:
            st.write("Nenhum exemplar cadastrado")
        else:
            op = st.selectbox("Exemplar", exs)
            disp = st.checkbox("Disponível", op.get_disponibilidade())
            if st.button("Atualizar"):
                View.exemplar_atualizar(op.get_id(), disp, op.get_codigo_livro())
                st.success("Exemplar atualizado")
                time.sleep(2)
                st.rerun()

    def excluir():
        exs = View.exemplar_listar()
        if len(exs) == 0:
            st.write("Nenhum exemplar cadastrado")
        else:
            op = st.selectbox("Exemplar", exs)
            if st.button("Excluir"):
                View.exemplar_excluir(op.get_id())
                st.success("Exemplar excluído")
                time.sleep(2)
                st.rerun()
