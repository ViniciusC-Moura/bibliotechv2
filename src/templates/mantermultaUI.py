import streamlit as st
import pandas as pd
import time
from views import View

class ManterMultaUI:

    def main():
        st.header("Cadastro de Multas")

        tab1, tab2, tab3, tab4 = st.tabs(
            ["Listar", "Inserir", "Atualizar", "Excluir"]
        )

        with tab1: ManterMultaUI.listar()
        with tab2: ManterMultaUI.inserir()
        with tab3: ManterMultaUI.atualizar()
        with tab4: ManterMultaUI.excluir()

    def listar():
        multas = View.multa_listar()

        if len(multas) == 0:
            st.write("Nenhuma multa cadastrada")
        else:
            dados = []
            for m in multas:
                dados.append({
                    "ID": m.get_id(),
                    "ID Empréstimo": m.get_id_emprestimo(),
                    "Valor": m.get_valor(),
                    "Descrição": m.get_descricao()
                })
            st.dataframe(pd.DataFrame(dados), use_container_width=True)

    def inserir():
        id_emprestimo = st.text_input("ID do empréstimo")
        valor = st.text_input("Valor da multa")
        descricao = st.text_input("Descrição")

        if st.button("Inserir"):
            View.multa_inserir(id_emprestimo, valor, descricao)
            st.success("Multa cadastrada com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        multas = View.multa_listar()

        if len(multas) == 0:
            st.write("Nenhuma multa cadastrada")
        else:
            op = st.selectbox("Selecione a multa", multas)

            valor = st.text_input("Valor", op.get_valor())
            descricao = st.checkbox("Descrição", op.get_descricao())

            if st.button("Atualizar"):
                View.multa_atualizar(
                    op.get_id(),
                    op.get_id_emprestimo(),
                    valor,
                    descricao
                )
                st.success("Multa atualizada com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        multas = View.multa_listar()

        if len(multas) == 0:
            st.write("Nenhuma multa cadastrada")
        else:
            op = st.selectbox("Selecione a multa", multas)

            if st.button("Excluir"):
                View.multa_excluir(op.get_id())
                st.success("Multa excluída com sucesso")
                time.sleep(2)
                st.rerun()
