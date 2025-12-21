# Caso 4 – Registrar devolução

## Atores envolvidos:
**Bibliotecário**: Ator primário

**Usuário (professor/aluno)**: Ator interessado

## Fluxo principal de eventos:
**1. [IN]** Bibliotecário acessa a seção “Empréstimos ativos”.  
**2. [IN]** Bibliotecário seleciona o empréstimo correspondente ao exemplar devolvido.  
**3. [OUT]** Sistema exibe os dados do empréstimo (usuário, livro, data prevista de devolução).  
**4. [IN]** Bibliotecário confirma o registro da devolução.  
**5. [OUT]** Sistema verifica se há atraso na devolução.  
**6. [OUT]** Sistema atualiza o status do exemplar para “disponível”.  
**7. [OUT]** Sistema encerra o empréstimo.  

## Fluxos alternativos:
### 5a. Devolução com atraso

**5a.1 [OUT]** Sistema calcula o valor da multa com base no período de atraso  
**5a.2 [OUT]** Sistema registra a multa associada ao usuário  
**5a.3 [OUT]** Sistema atualiza o status do exemplar para “disponível”  
**5a.4 [OUT]** Sistema encerra o empréstimo  

### 6a. Exemplar possui reserva pendente

**6a.1 [OUT]** Sistema identifica a existência de reserva ativa para o exemplar.  
**6a.2 [OUT]** Sistema atualiza o status do exemplar para “reservado”.

---

**Pré-condições:**
- O bibliotecário deve estar autenticado no sistema.
- Deve existir ao menos um empréstimo ativo registrado no sistema.

**Pós-condições:**  
- O empréstimo é encerrado no sistema.
- O status do exemplar é atualizado para disponível ou reservado, conforme a existência de reservas pendentes.
- Em caso de atraso, a multa correspondente é registrada para o usuário.