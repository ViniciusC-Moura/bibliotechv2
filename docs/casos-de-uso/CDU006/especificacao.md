# Caso 6 – Reservar Livro

## Atores envolvidos:
**Usuário (Aluno/Professor)**: Ator primário

## Fluxo principal de eventos:
**1. [IN]** Usuário acessa a funcionalidade “Consultar livros”.  
**2. [IN]** Usuário seleciona o livro desejado.  
**3. [OUT]** Sistema exibe os detalhes do livro e a agenda de disponibilidade.  
**4. [IN]** Usuário informa a data de início e a data de término desejadas para o empréstimo.  
**5. [OUT]** Sistema verifica conflito de datas com outros empréstimos ou reservas existentes do exemplar.  
**6. [OUT]** Sistema registra a solicitação de empréstimo com status “pendente”.  
**7. [OUT]** Sistema informa ao usuário que a solicitação foi enviada para análise do bibliotecário.

## Fluxos alternativos:
### 5a. Conflito de datas identificado
<sub>(ex.: único exemplar já reservado ou emprestado no período solicitado)</sub>

**5a.1 [OUT]** Sistema informa ao usuário que o período selecionado não está disponível.  
**5a.2 [OUT]** Sistema solicita a escolha de um novo período.

### 6a. Exemplar possui reserva pendente

**6a.1 [OUT]** Sistema identifica a existência de reserva ativa para o exemplar.  
**6a.2 [OUT]** Sistema atualiza o status do exemplar para “reservado”.

---

**Pré-condições:**
- O usuário deve estar autenticado no sistema como Aluno ou Professor.

**Pós-condições:**  
- Uma solicitação de empréstimo é registrada com status pendente.
- A solicitação fica disponível para análise no **CDU003 – Realizar Empréstimo.**
- Em caso de conflito, nenhuma solicitação é registrada.