import inquirer

from todolist import ListaTarefas

tarefas = ListaTarefas()

while True:
  resposta_do_menu = inquirer.prompt([
    inquirer.List('option',
      message='Escolha uma das opções abaixo:',
      choices=[
          ('Adicionar tarefa', 'adicionar'),
          ('Alterar status da tarefa', 'alterar'),
          ('Remover tarefa', 'remover'),
          ('Visualizar tarefas', 'vizualizar'),
          ('Fechar', 'encerrar')
      ]
    )
  ])

  opcao_selecionada_do_menu = resposta_do_menu['option']

  if opcao_selecionada_do_menu == 'encerrar':
    break

  if opcao_selecionada_do_menu == 'adicionar':
    dados_da_tarefa = inquirer.prompt([
      inquirer.Text("title", message="Qual o nome da tarefa?"),
      inquirer.Text("date", message="Insira a data de quando essa tarefa tem que ser entregue?")
    ])

    tarefas.adicionar_tarefa(dados_da_tarefa['title'], dados_da_tarefa['date'])

    print('Tarefa adicionada com sucesso!')


  if opcao_selecionada_do_menu == 'alterar':
    dados_da_tarefa = inquirer.prompt([
      inquirer.Text("title", message="Qual o nome da tarefa?"),
    ])

    tarefas.alterar_status_tarefa(dados_da_tarefa['title'])


  if opcao_selecionada_do_menu == 'remover':
    dados_da_tarefa = inquirer.prompt([
      inquirer.Text("title", message="Qual o nome da tarefa?"),
      inquirer.Confirm(
        "confirmation",
        message="Você deseja realmente remover essa terefa?",
        default=False,
      ),
    ])

    if dados_da_tarefa['confirmation']:
        tarefas.remover_tarefa(dados_da_tarefa['title'])


  if opcao_selecionada_do_menu == 'vizualizar':
    dados_da_tarefa = inquirer.prompt([
      inquirer.Text("date", message="Insira a data das tarefas que deseja vizualizar")
    ])

    data = dados_da_tarefa['date']
    tarefas = tarefas.visualizar_tarefas(data)

    print(f'Lista de tarefas para a data {data}:')

    for tarefa in tarefas:
      print(f'Titulo: {tarefa[0]} | Data: {tarefa[1]} | Status: {tarefa[2]}')

    print('\n')
