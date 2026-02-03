import streamlit as st
import pandas as pd
import time
from views import View

class ManterEmprestimoUI:

    def main():
        st.header("Cadastro de Empréstimos")

        tab1, tab2, tab3, tab4 = st.tabs(
            ["Listar", "Inserir", "Atualizar", "Excluir"]
        )

        with tab1: ManterEmprestimoUI.listar()
        with tab2: ManterEmprestimoUI.inserir()
        with tab3: ManterEmprestimoUI.atualizar()
        with tab4: ManterEmprestimoUI.excluir()

    def listar():
        emprestimos = View.emprestimo_listar()

        if len(emprestimos) == 0:
            st.write("Nenhum empréstimo cadastrado")
        else:
            dados = []
            for e in emprestimos:
                dados.append({
                    "ID": e.get_id(),
                    "CPF Usuário": e.get_cpf_usuario(),
                    "ID Exemplar": e.get_id_exemplar(),
                    "Data Empréstimo": e.get_dt_emprestimo(),
                    "Data Devolução": e.get_dt_devolucao(),
                    "Confirmado": e.get_confirmado()
                })
            st.dataframe(pd.DataFrame(dados), use_container_width=True)

    def inserir():
        cpf_usuario = st.text_input("CPF do usuário")
        id_exemplar = st.text_input("ID do exemplar")
        dt_emprestimo = st.text_input("Data do empréstimo")
        dt_prazo = st.text_input("Prazo de entrega")
        confirmado = st.checkbox("Confirmado?")

        if st.button("Inserir"):
            View.emprestimo_inserir(dt_emprestimo, dt_prazo, cpf_usuario, id_exemplar, confirmado)
            st.success("Empréstimo cadastrado com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        emprestimos = View.emprestimo_listar()

        if len(emprestimos) == 0:
            st.write("Nenhum empréstimo cadastrado")
        else:
            op = st.selectbox("Selecione o empréstimo", emprestimos)

            data_emp = st.text_input(
                "Data do empréstimo", op.get_dt_emprestimo()
            )
            data_dev = st.text_input(
                "Data da devolução", op.get_dt_devolucao()
            )
            confirmado = st.checkbox("Confirmado", op.get_confirmado())

            if st.button("Atualizar"):
                View.emprestimo_atualizar(
                    op.get_id(),
                    data_emp,
                    op.get_dt_prazo(),
                    data_dev,
                    op.get_cpf_usuario(),
                    op.get_id_exemplar(),
                    confirmado
                )
                st.success("Empréstimo atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        emprestimos = View.emprestimo_listar()

        if len(emprestimos) == 0:
            st.write("Nenhum empréstimo cadastrado")
        else:
            op = st.selectbox("Selecione o empréstimo a ser excluído", emprestimos)

            if st.button("Excluir"):
                View.emprestimo_excluir(op.get_id())
                st.success("Empréstimo excluído com sucesso")
                time.sleep(2)
                st.rerun()
