import streamlit as st
from views import View

class LoginUI:
    def main():
        st.header("Entrar no Sistema")
        cpf = st.text_input("Informe o cpf")
        senha = st.text_input("Informe a senha", type="password")
        if st.button("Entrar"):
            u = View.usuario_autenticar(cpf, senha)
            b = View.bibliotecario_autenticar(cpf, senha)
            if b: 
                st.session_state["client_nivel"] = "bibliotecario"
                client = b
                nome = "Bibliotecário"
            if u:
                st.session_state["client_nivel"] = "usuario"
                client = u
                nome = client["nome"]
            if u == None and b == None: st.write("CPF ou senha inválidos")
            else:
                st.session_state["client_cpf"] = client["cpf"]
                st.session_state["client_nome"] = nome
                st.rerun()
                