# TodoList: Projeto de POO
Por Matheus Goya e Victória Nedina em módulo de Python no Bootcamp Itaú Dados da Let's Code.

# Requisitos Funcionais

A aplicação deve dispor de um menu com as seguintes opções para o usuário:

1. **Adicionar tarefa:** Ao solicitar essa opção o usuário poderá criar uma nova tarefa. Para isso, ele deverá informar o título, a data de realização e a categoria da tarefa. Você deverá salvar essas três informações (além de uma informação de que o status da tarefa está como *Pendente*) dentro de um arquivo CSV (`tarefas.csv`, por exemplo).
2. **Alterar status da Tarefa:** Ao solicitar essa opção o usuário poderá alterar o status de uma determinada tarefa, ou seja, se a tarefa está como *Pendente*, ficará como *Concluída*, e vice-versa. Para isso, ele deve informar o título da tarefa. Você deverá alterar a coluna de *Status* do arquivo, referente à tarefa que possui o título informado pelo usuário.
3. **Remover tarefa:** Ao solicitar essa opção o usuário poderá escolher uma tarefa para que essa seja removida. Para isso, ele deve informar o título da tarefa. Você deve remover a linha do arquivo que contém a tarefa cujo título foi informado pelo usuário.
4. **Visualizar tarefas:** Ao solicitar essa opção o usuário poderá escolher um dia específico para ver as tarefas agendadas para ele. Para isso, após escolher essa opção, o usuário precisa informar uma data. Você deve procurar pelas atividades que estão programadas para aquele dia específico (dentro do arquivo csv), e exibir todas elas.
5. **Fechar:** Ao solicitar essa opção o programa deverá ser encerrado.

# Instruções do Projeto

- O projeto deve ser realizado em grupo, sendo cada um composto por 2 integrantes.
- O projeto deve ser desenvolvido utilizando o Git, e os commits devem ser realizados por ambos os integrantes da equipe. Lembrando que isso ficará guardado no histórico de commits do projeto.
- **O projeto deve ser realizado com a utilização do conceito de Orientação a Objetos.** Ou seja, você deve pensar na lista de tarefas como uma classe que possui atributos e métodos.
- Embora a estrutura do projeto deva ter os requisitos funcionais citados na seção anterior, sinta-se à vontade para alterar ou até acrescentar outras features. Por exemplo:
    - Você pode querer criar um submódulo com funções que executem algo que você costuma fazer com mais frequência.
    - Você pode adicionar mais opções para o usuário, como editar uma tarefa.
    - Você pode permitir que, no momento da criação de uma tarefa, o usuário possa digitar a data como sendo *hoje* ou *amanhã*, além do formato convencional (`dd/mm/aaaa`).
    - Você pode remover ou alterar o status de uma tafera com base no título e, também, na data (caso haja tarefas com o mesmo título); dessa forma, você evita remover tarefas que possuem o mesmo título.
