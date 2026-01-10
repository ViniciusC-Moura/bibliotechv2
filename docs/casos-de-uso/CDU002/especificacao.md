# caso 2 - Cadastrar usuário

## Atores envolvidos:
**Usuário (professor/aluno)**: Ator primário

**Pré-condições:**
- O bibliotecário deve estar autenticado no sistema.
- A pessoa deve ser professor ou aluno da instituição.

**Pós-condições:**  
- A pessoa se torna um usuário.
- A pessoa passa a conseguir realizar empréstimos de livros.

## Fluxo principal de eventos:
**1. [IN]** A pessoa solicita ao bibliotecário no balcão para realizar o cadastro.  
**2. [IN]** O bibliotecário solicita os dados para a pessoa.  
**3. [IN]** A pessoa informa ao bibliotecário os dados para serem preenchidos no formulário.  
**4. [OUT]** O sistema aprova os dados da pessoa.     

## Fluxos alternativos:
### 4a. Preenchimento incorreto dos dados
**3a.1[OUT]** Sistema detecta algum dado preenchido incorretamente.  
**3a.2[OUT]** Sistema destaca os campos em vermelho e exibe a mensagem:"Campo inválido".  
**3a.3[IN]** O bibliotecário solicita a revisão dos dados informados.  