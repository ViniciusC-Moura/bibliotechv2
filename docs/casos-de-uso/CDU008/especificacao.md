# caso 8 - Emitir multa

## Atores envolvidos:
**Bibliotecário**: Ator primário

**Pré-condições:**
- O bibliotecário deve estar autenticado no sistema.
- Deve haver uma devolução registrada.
**Pós-condições:**  
- Uma multa ficará registrada no cadastro do usuário.
## Fluxo principal de eventos:
**1. [IN]**O usuário realiza a devolução do livro.  
**2. [IN]** O bibliotecário acessa a funcionalidade "Historico de empréstimos".  
**3. [OUT]** O sistema informa que houve atraso na devolução daquele exemplar.  
**4. [OUT]** O sistema calcula o valor da multa com base na quantidade de dias atrasados na devolução.  
**5. [IN]** O bibliotecário aprova a emissão da multa. 
**6. [OUT]** O Sistema registra uma multa vinculada àquele empréstimo
