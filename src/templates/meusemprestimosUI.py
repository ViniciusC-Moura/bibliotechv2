import streamlit as st
from views import View
from datetime import date

class MeusEmprestimosUI:
    def main():
        st.header("Seus empréstimos:")

        op = View.usuario_listar_cpf(st.session_state["client_cpf"])
        emprestimos = [em for em in View.emprestimo_listar() if em.get_cpf_usuario() == op.get_cpf()]
        emprestimos.sort(key=lambda em: em.get_dt_emprestimo())

        st.divider()
        
        if not emprestimos: st.info("Você não tem empréstimos registrados")
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

                    if not emp.get_confirmado(): status = "Solicitado"
                    elif dt_devolucao and dt_devolucao > dt_prazo: status = "Devolvido com atraso"
                    elif dt_devolucao: status = "Devolvido"
                    elif hoje < dt_inicio: status = "Agendado"
                    elif hoje > dt_prazo: status = "Atrasado"
                    else: status = "Em andamento"

                    multas = [m for m in View.multa_listar() if m.get_id_emprestimo() == emp.get_id()]

                    st.write(f"📅 **Data de início:** {emp.get_dt_emprestimo()}")
                    st.write(f"⏳ **Prazo de devolução:** {emp.get_dt_prazo()}")
                    st.write(f"📥 **Data de devolução:** {emp.get_dt_devolucao()}")
                    st.write(f"📚 **Livro:** {livro.get_nome()}")
                    st.write(f"📌 **Status:** {status}")
                    
                    if multas:
                        st.subheader("Multa(s):")
                        for m in multas:
                            st.write(f"**Multa**: {m.get_valor()}")
                            st.write(f"**Descrição**: {m.get_descricao()}")

                    st.divider()
