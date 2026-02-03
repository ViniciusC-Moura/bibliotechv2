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
        autores = View.autor_listar()
        livros = View.livro_listar()

        if not autores or not livros:
            st.warning("É necessário ter autores e livros cadastrados")
            return

        autor = st.selectbox("Autor", autores)
        livro = st.selectbox("Livro", livros)

        if st.button("Inserir", key="autoria_inserir"):
            autorias = View.autoria_listar()

            for a in autorias:
                if a.get_id_autor() == autor.get_id() and a.get_codigo_livro() == livro.get_codigo():
                    st.warning("Essa autoria já está cadastrada")
                    return

            View.autoria_inserir(autor.get_id(), livro.get_codigo())
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
