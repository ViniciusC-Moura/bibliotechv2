# caso 2 - Cadastrar usuário

## Atores envolvidos:
**Usuário (professor/aluno)**: Ator primário

**Pré-condições:**
- O bibliotecário deve estar autenticado no sistema.
- O visitante deve ser professor ou aluno da instituição.

**Pós-condições:**  
- Cadastro do usuário está registrado no sistema.

## Fluxo principal de eventos:
**1. [IN]** O visitante solicita ao bibliotecário presente no balcão para realizar o cadastro.  
**2. [IN]** O bibliotecário acessa a funcionalidade "Cadastrar usuário".  
**3. [OUT]** Sistema exibe um formulário de preenchimento dos dados do usuário.   
**4. [IN]** O visitante informa ao bibliotecário os dados a serem preenchidos no formulário.  
**5. [OUT]** O sistema faz a verificação dos dados.  
**6. [OUT]** O sistema registra o usuário.  
**7. [OUT]** O sistema informa ao bibliotecário que o cadastro foi aprovado.   
**8. [IN]** O bibliotecário informa ao visitante que o cadastro foi aprovado.  

## Fluxos alternativos:
### 4a. Preenchimento incorreto dos dados
**3a.1[OUT]** Sistema detecta algum dado preenchido incorretamente.  
**3a.2[OUT]** Sistema destaca os campos em vermelho e exibe a mensagem:"Campo inválido".  
**3a.3[IN]** O bibliotecário solicita a revisão dos dados informados.  