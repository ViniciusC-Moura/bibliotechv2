import streamlit as st
from views import View
from datetime import date

class CatalogoUI:
    def main():
        st.header("Catálogo de livros")

        for livro in View.livro_listar():
            autores = ", ".join(View.livro_get_autores(livro.get_codigo()))
            st.subheader(livro.get_nome())
            st.write(f"Autor(es): {autores}")
            
            exemplares = View.livro_get_exemplares(livro.get_codigo())

            with st.expander("Reservar"):
                data_inicio = st.date_input(f"Data de início - {livro.get_nome()}", value=date.today())
                data_fim = st.date_input(f"Data de fim - {livro.get_nome()}", value=date.today())

                periodos_exemplares = {}  # chave: exemplar_id, valor: lista de tuplas (inicio, fim)
                for e in exemplares:
                    periodos = []
                    for em in View.emprestimo_listar():
                        if em.get_id_exemplar() == e.get_id() and em.get_confirmado() and em.get_dt_devolucao() is None:
                            periodos.append((em.get_dt_emprestimo(), em.get_dt_prazo()))
                    periodos.sort(key=lambda x: x[0])
                    periodos_exemplares[e.get_id()] = periodos

                if len(exemplares) == 1:
                    periodos = periodos_exemplares[exemplares[0].get_id()]
                    if periodos:
                        texto_periodos = ", ".join(f"{inicio.day}-{fim.day} {inicio.strftime('%b')}" for inicio, fim in periodos)
                        st.info(f"Datas indisponíveis: {texto_periodos}")

                if st.button(f"Reservar {livro.get_nome()}", key=livro.get_codigo()):
                    if data_fim <= data_inicio:
                        st.error("O empréstimo deve ter pelo menos 1 dia")
                        continue

                    exemplar_escolhido = None
                    for e in exemplares:
                        livre = True
                        for inicio, fim in periodos_exemplares[e.get_id()]:
                            if data_inicio <= fim and data_fim >= inicio:
                                livre = False
                                break
                        if livre:
                            exemplar_escolhido = e
                            break

                    if not exemplar_escolhido:
                        st.error("Não há exemplares disponíveis nesse período")
                    else:
                        View.emprestimo_inserir(
                            data_inicio,
                            data_fim,
                            st.session_state["client_cpf"],
                            exemplar_escolhido.get_id(),
                            False
                        )
                        st.success(f"Livro '{livro.get_nome()}' reservado de {data_inicio} até {data_fim}!")
            st.divider()
