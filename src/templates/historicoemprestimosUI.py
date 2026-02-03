import streamlit as st
from views import View
from datetime import date
import time

class HistoricoEmprestimosUI:
    def main():
        st.header("Histórico de empréstimos")

        usuarios = View.usuario_listar()
        op = st.selectbox("Selecione o usuário", usuarios)
        emprestimos = [em for em in View.emprestimo_listar() if em.get_cpf_usuario() == op.get_cpf()]
        emprestimos.sort(key=lambda em: em.get_dt_emprestimo())

        st.subheader(op.get_nome())
        st.divider()
        
        if not emprestimos: st.info("Esse usuário não tem empréstimos registrados")
        else:
            for emp in emprestimos:
                    exemplar = View.exemplar_listar_id(emp.get_id_exemplar())
                    livro = View.livro_listar_codigo(exemplar.get_codigo_livro())

                    dt_inicio = date.fromisoformat(emp.get_dt_emprestimo())
                    dt_prazo  = date.fromisoformat(emp.get_dt_prazo())
                    dt_devolucao = None
                    if emp.get_dt_devolucao():
                        dt_devolucao = date.fromisoformat(emp.get_dt_devolucao())
                    hoje = date.today()

                    if dt_devolucao and dt_devolucao > dt_prazo:
                        status = "Devolvido com atraso"
                        valor_multa = (dt_devolucao - dt_prazo).days * 10.0
                    elif dt_devolucao: status = "Devolvido"
                    elif hoje < dt_inicio: status = "Agendado"
                    elif hoje > dt_prazo:
                        status = "Atrasado"
                        valor_multa = (hoje - dt_prazo).days * 10.0
                    else: status = "Em andamento"

                    multas = [m for m in View.multa_listar() if m.get_id_emprestimo() == emp.get_id()]

                    st.write(f"📅 **Data de início:** {emp.get_dt_emprestimo()}")
                    st.write(f"⏳ **Prazo de devolução:** {emp.get_dt_prazo()}")
                    st.write(f"📥 **Data de devolução:** {emp.get_dt_devolucao()}")
                    st.write(f"📚 **Livro:** {livro.get_nome()}")
                    st.write(f"📌 **Status:** {status}")

                    if (status in ["Devolvido com atraso", "Atrasado"]) and not multas:
                        if st.button(f"Multar - R${valor_multa}", key=f"multa_{emp.get_id()}"):
                            View.multa_inserir(emp.get_id(), valor_multa, f"Atraso: {valor_multa/10} dias")
                            st.success("Multa atribuída.")
                            time.sleep(2)
                            st.rerun()


                    st.divider()
