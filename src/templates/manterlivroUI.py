import streamlit as st
import pandas as pd
import time
from views import View


class ManterLivroUI:

    def main():
        st.header("Cadastro de Livros")

        tab1, tab2, tab3, tab4 = st.tabs(
            ["Listar", "Inserir", "Atualizar", "Excluir"]
        )

        with tab1:
            ManterLivroUI.listar()
        with tab2:
            ManterLivroUI.inserir()
        with tab3:
            ManterLivroUI.atualizar()
        with tab4:
            ManterLivroUI.excluir()

    def listar():
        livros = View.livro_listar()

        if len(livros) == 0:
            st.write("Nenhum livro cadastrado")
        else:
            dados = []
            for l in livros:
                dados.append({
                    "Código": l.get_codigo(),
                    "Nome": l.get_nome()
                })

            df = pd.DataFrame(dados)
            st.dataframe(df, use_container_width=True)

    def inserir():
        codigo = st.text_input("Código do livro")
        nome = st.text_input("Nome do livro")

        if st.button("Inserir"):
            View.livro_inserir(codigo, nome)
            st.success("Livro cadastrado com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        livros = View.livro_listar()

        if len(livros) == 0:
            st.write("Nenhum livro cadastrado")
        else:
            op = st.selectbox("Selecione o livro", livros)
            nome = st.text_input("Novo nome", op.get_nome())

            if st.button("Atualizar"):
                View.livro_atualizar(op.get_codigo(), nome)
                st.success("Livro atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        livros = View.livro_listar()

        if len(livros) == 0:
            st.write("Nenhum livro cadastrado")
        else:
            op = st.selectbox("Selecione o livro", livros)

            if st.button("Excluir"):
                View.livro_excluir(op.get_codigo())
                st.success("Livro excluído com sucesso")
                time.sleep(2)
                st.rerun()
