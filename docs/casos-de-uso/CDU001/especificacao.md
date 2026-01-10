# Caso 1 - Cadastrar livro

## Atores envolvidos:
**Bibliotecário**: Ator primário

**Pré-condições:**
- O bibliotecário deve estar autenticado no sistema.

**Pós-condições:**  
- O livro é cadastrado no sistema e fica disponível para professores e alunos.
- O status dos exemplares do livro são atualizados para disponível.

## Fluxo principal de eventos:
**1. [IN]** Bibliotecário acessa a funcionalidade "Cadastrar livros".  
**2. [OUT]** Sistema exibe um formulário de preenchimento dos dados do livro (título, quantidade de páginas, descrição, gênero, Autor).  
**3. [IN]** Bibliotecário preenche os campos com os dados requeridos pelo sistema no formulário.  
**4. [OUT]** Sistema consulta o banco de dados para verificação dos dados.  
**5. [OUT]** Sistema registra o livro no acervo.  
**6. [OUT]** Sistema informa ao bibliotecário que o cadastro do livro foi aprovado.  

## Fluxos alternativos:
### 4a. Preenchimento incorreto dos dados
**4a.1[OUT]** Sistema detecta algum dado preenchido incorretamente.  
**4a.2[OUT]** Sistema destaca os campos em vermelho e exibe a mensagem:"Campo inválido".  

### 4a. Livro já existente
**4a.1[OUT]** Sistema constata a existência do livro no acervo.  
**4a.2[OUT]** Sistema informa ao bibliotecário que o livro já está cadastrado no acervo.  