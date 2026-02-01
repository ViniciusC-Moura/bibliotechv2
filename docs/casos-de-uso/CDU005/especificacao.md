# Caso 5 – Consultar próprio histórico de empréstimos

## Atores envolvidos:
**Usuário (Aluno/Professor)**: Ator primário

## Pré-condições:
- O usuário deve estar autenticado no sistema como Aluno ou Professor.
- Deve existir ao menos um usuário cadastrado no sistema.

## Pós-condições:
- O usuário visualiza seu histórico de empréstimos, incluindo:
  - datas de início e prazo;
  - data de devolução (quando existente);
  - status do empréstimo;
  - multas associadas (quando houver).

## Fluxo principal de eventos:
**1. [IN]** Usuário acessa a funcionalidade “Meus empréstimos”.  
**2. [OUT]** Sistema identifica o usuário autenticado e recupera seus empréstimos registrados.  
**3. [OUT]** Sistema ordena os empréstimos por data de início.  
**4. [OUT]** Sistema exibe, para cada empréstimo, as seguintes informações:  
- data de início do empréstimo;  
- prazo de devolução;  
- data de devolução (se houver);  
- título do livro;  
- status do empréstimo.  
**5. [OUT]** Sistema exibe as multas associadas ao empréstimo, quando existentes.  

## Fluxos alternativos:

### 2a. Usuário sem empréstimos registrados
**2a.1 [OUT]** Sistema informa que o usuário não possui empréstimos registrados.  

### 4a. Empréstimo ainda não confirmado
**4a.1 [OUT]** Sistema exibe o status do empréstimo como “Solicitado”.  

### 4b. Empréstimo devolvido com atraso
**4b.1 [OUT]** Sistema exibe o status do empréstimo como “Devolvido com atraso”.  
**4b.2 [OUT]** Sistema exibe as multas associadas ao empréstimo.  

### 4c. Empréstimo atrasado
**4c.1 [OUT]** Sistema exibe o status do empréstimo como “Atrasado”.  

### 4d. Empréstimo agendado
**4d.1 [OUT]** Sistema exibe o status do empréstimo como “Agendado”.  

### 4e. Empréstimo em andamento
**4e.1 [OUT]** Sistema exibe o status do empréstimo como “Em andamento”.  
