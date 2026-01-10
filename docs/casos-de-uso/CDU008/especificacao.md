# caso 8 - Emitir multa

## Atores envolvidos:
**Bibliotecário**: Ator primário

**Pré-condições:**
- O bibliotecário deve estar autenticado no sistema.
- Deve haver uma devolução registrada.
**Pós-condições:**  
- Uma multa ficará registrada no cadastro do usuário.
- O usuário não pode reservar livros enquanto não realizar o pagamento.
## Fluxo principal de eventos:
**1. [IN]**O usuário realiza a devolução do livro.  
**2. [IN]** O bibliotecário acessa a funcionalidade "Emitir multa".  
**3. [OUT]** O sistema informa que houve atraso na devolução daquele exemplar.  
**4. [OUT]** O sistema calcula o valor da multa com base na quantidade de dias atrasados na devolução.  
**5. [IN]** O bibliotecário aprova a emissão da multa. 
**6. [OUT]** O Sistema atualiza o status do usuário para "Inadimplente" e bloqueia novas reservas automaticamente.  

## Fluxos alternativos:
### 5a. Isenção de multa
**5a.1[IN]** O Bibliotecário solicita a isenção da multa.  
**5a.2[OUT]** O Sistema requere uma justificativa obrigatória para a isenção.  
**5a.3[IN]** O Bibliotecário insere o motivo.  
**5a.4[OUT]** O Sistema registra a devolução, mas não gera o débito financeiro no cadastro do usuário.  