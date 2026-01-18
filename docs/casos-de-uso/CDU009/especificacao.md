# caso 9 - Verificar disponibilidade dos livros

## Atores envolvidos:
**Bibliotecário**: Ator primário
**Usuário (professor/aluno)**: Ator primário

**Pré-condições:**
- O consulente deve estar autenticado no sistema.
**Pós-condições:**  

## Fluxo principal de eventos:
**1. [IN]** O consulente acessa a funcionalidade "Verificar disponibilidade dos livros".  
**2. [OUT]** O sistema mostra todos os livros do acervo.  
**3. [IN]** O consulente pesquisa o livro que ele deseja ver a disponibilidade.  
**4. [IN]** O consulente acessa as especificações do livro.  

## Fluxos alternativos:
### 3a. Livro não encontrado
**3a.1[OUT]** O sistema informa que nenhum livro foi encontrado.  
**3a.2[IN]** O consulente opta por fazer uma nova pesquisa.  