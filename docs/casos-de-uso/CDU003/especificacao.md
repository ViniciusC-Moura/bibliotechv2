# Caso 3 – Realizar Empréstimo

## Atores envolvidos:
**Bibliotecário**: Ator primário

**Usuário (professor/aluno)**: Ator interessado. Inicia o processo no CDU  "Reservar livro"
## Fluxo principal de eventos:
**1. [IN]** Bibliotecário entra na seção “solicitações”  
**2. [IN]** Bibliotecário seleciona uma solicitação pendente  
**3. [OUT]** Sistema mostra se o livro está disponível  
**4. [IN]** Bibliotecário permite o empréstimo  
**5. [OUT]** Sistema registra um exemplar como “emprestado” durante o período informado pela solicitação  

## Fluxo alternativo:
### 4a. Bibliotecário nega a solicitação

**4a. [IN]** Bibliotecário não permite o empréstimo  
**5a. [OUT]** Sistema informa o remetente da solicitação que ela foi negada  

---

**Pré-condições:**
- O bibliotecário deve estar autenticado no sistema.
- Deve existir ao menos uma solicitação de empréstimo registrada.

**Pós-condições:**  
- A solicitação é processada como aprovada ou negada.
- Em caso de aprovação, o exemplar tem seu status atualizado para emprestado.
