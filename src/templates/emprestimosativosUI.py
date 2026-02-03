import streamlit as st
from views import View
from datetime import date
import time

class EmprestimosAtivosUI:
    def main():
        st.header("Empréstimos ativos")

        emprestimos = [em for em in View.emprestimo_listar() if not em.get_dt_devolucao() and em.get_confirmado()]
        emprestimos.sort(key=lambda em: em.get_dt_emprestimo())

        if not emprestimos: st.info("Não há empréstimos cadastrados")
        else:
            for emp in emprestimos:
                    exemplar = View.exemplar_listar_id(emp.get_id_exemplar())
                    livro = View.livro_listar_codigo(exemplar.get_codigo_livro())

                    dt_prazo  = date.fromisoformat(emp.get_dt_prazo())
                    hoje = date.today()

                    if hoje > dt_prazo: status = "Atrasado"
                    else: status = "Em andamento"

                    st.write(f"📅 **Data de início:** {emp.get_dt_emprestimo()}")
                    st.write(f"⏳ **Prazo de devolução:** {emp.get_dt_prazo()}")
                    st.write(f"📚 **Livro:** {livro.get_nome()}")
                    st.write(f"📌 **Status:** {status}")

                    if st.button("Registrar devolução", key=f"emprestimo_{emp.get_id()}"):
                        View.emprestimo_devolver(emp.get_id(), hoje)
                        st.success("Devolução registrada")
                        time.sleep(2)
                        st.rerun()

                    st.divider()
