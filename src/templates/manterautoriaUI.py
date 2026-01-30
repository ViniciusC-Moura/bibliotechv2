import streamlit as st
import pandas as pd
import time
from views import View

class ManterAutoriaUI:

    def main():
        st.header("Cadastro de Autorias")

        tab1, tab2, tab3, tab4 = st.tabs(
            ["Listar", "Inserir", "Atualizar", "Excluir"]
        )

        with tab1: ManterAutoriaUI.listar()
        with tab2: ManterAutoriaUI.inserir()
        with tab3: ManterAutoriaUI.atualizar()
        with tab4: ManterAutoriaUI.excluir()

    def listar():
        autorias = View.autoria_listar()

        if len(autorias) == 0:
            st.write("Nenhuma autoria cadastrada")
        else:
            dados = []
            for a in autorias:
                dados.append({
                    "Livro": a.get_codigo_livro(),
                    "Autor": a.get_id_autor()
                })
            st.dataframe(pd.DataFrame(dados), use_container_width=True)

    def inserir():
        id_autor = st.text_input("ID do autor")
        codigo_livro = st.text_input("Código do livro")


        if st.button("Inserir", key="autoria_inserir"):
            View.autoria_inserir(int(id_autor), int(codigo_livro))
            st.success("Autoria cadastrada com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        st.info("Atualização não prevista para autoria")

    def excluir():
        autorias = View.autoria_listar()

        if len(autorias) == 0:
            st.write("Nenhuma autoria cadastrada")
        else:
            op = st.selectbox("Selecione a autoria a ser excluída", autorias)

            if st.button("Excluir", key="autoria_excluir"):
                View.autoria_excluir(op.get_id_autor(), op.get_codigo_livro())

                st.success("Autoria excluída com sucesso")
                time.sleep(2)
                st.rerun()
