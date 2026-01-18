# Caso 7 - Consultar histórico de empréstimo

## Atores envolvidos:
**Bibliotecário**: Ator primário

**Pré-condições:**
- O bibliotecário deve estar autenticado no sistema.
**Pós-condições:**  

## Fluxo principal de eventos:
**1. [IN]** O bibliotecário acessa a funcionalidade "Consultar histórico de empréstimo".  
**2. [OUT]** O sistema mostra o cadastro de todos os usuários.  
**3. [IN]** O bibliotecário pesquisa o usuário que ele deseja consultar histórico.  
**4. [IN]** O bibliotecário acessa o cadastro do usuário.   

## Fluxos alternativos:
### 3a. Usuário não encontrado
**3a.1[OUT]** O sistema informa que nenhum usuário foi encontrado.  
**3a.2[IN]** O bibliotecário opta por fazer uma nova pesquisa.  