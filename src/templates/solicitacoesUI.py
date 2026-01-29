import streamlit as st
from views import View
import time

class SolicitacoesUI:
    def main():
        st.header("Solicitações de Empréstimo")

        solicitacoes = [em for em in View.emprestimo_listar() if not em.get_confirmado()]
        solicitacoes.sort(key=lambda em: em.get_dt_emprestimo())

        if not solicitacoes:
            st.info("Nenhuma solicitação pendente.")
            return

        for emp in solicitacoes:
            exemplar = View.exemplar_listar_id(emp.get_id_exemplar())
            livro = View.livro_listar_codigo(exemplar.get_codigo_livro())

            with st.container():
                st.subheader(livro.get_nome())

                st.write(f"📅 **Data de início:** {emp.get_dt_emprestimo()}")
                st.write(f"⏳ **Prazo de devolução:** {emp.get_dt_prazo()}")
                st.write(f"👤 **CPF do usuário:** {emp.get_cpf_usuario()}")
                st.write(f"📚 **Livro:** {livro.get_nome()}")

                col1, col2 = st.columns(2)

                with col1:
                    if st.button("Confirmar", key=f"conf_{emp.get_id()}"):
                        View.emprestimo_confirmar(emp.get_id())
                        st.success("Empréstimo confirmado!")
                        time.sleep(2)
                        st.rerun()

                with col2:
                    if st.button("Recusar", key=f"rec_{emp.get_id()}"):
                        View.emprestimo_excluir(emp.get_id())
                        st.warning("Solicitação recusada.")
                        time.sleep(2)
                        st.rerun()

                st.divider()