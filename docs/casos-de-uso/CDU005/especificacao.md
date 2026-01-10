# Caso 5 - Renovar empréstimo

## Atores envolvidos:
**Bibliotecário**: Ator primário
**Usuário (professor/aluno)**: Ator interessado

**Pré-condições:**
- O usuário deve estar autenticado no sistema como Aluno ou Professor.
- O bibliotecário deve estar autenticado no sistema.
- Deve existir um empréstimo registrado.
**Pós-condições:**  
- Caso não haja nenhuma solicitação de reserva pendente pelo exemplar requerido, a solicitação é aprovada.
## Fluxo principal de eventos:
**1. [IN]** Bibliotecário entra na seção “solicitações de renovação”.  
**2. [IN]** Bibliotecário seleciona uma solicitação pendente.  
**3. [OUT]** Sistema mostra se não há nenhuma solicitação de reserva pendente pelo exemplar requerido.  
**4. [IN]** Bibliotecário permite a renovação do empréstimo.  
**5. [OUT]** Sistema registra um exemplar como “renovado” durante o período informado pela solicitação.     

## Fluxos alternativos:
### 3a. Reserva pendente
**3a.1[OUT]** Sistema constata solicitação de reserva pendente pelo exemplar requerido.
**3a.2[IN]** Bibliotecário nega a solicitação de renovação do empréstimo
