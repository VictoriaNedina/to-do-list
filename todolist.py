import csv


class ListaTarefas:
    def __init__(self):
        pass

    def _procurar_tarefa(self, titulo):
        with open('tarefas.csv') as arquivo:
            leitor = csv.reader(arquivo, delimiter=';', lineterminator='\n')
            for linha in leitor:
                if linha[0].strip().lower() == titulo.strip().lower():
                    return titulo
        return None

    def tarefa(self, titulo):
        with open('tarefas.csv') as arquivo:
            leitor = csv.reader(arquivo, delimiter=';', lineterminator='\n')
            for linha in leitor:
                if linha[0].strip().lower() == titulo.strip().lower():
                    return linha
        return None

    def adicionar_tarefa(self, titulo, data):
        tarefa_procurada = self._procurar_tarefa(titulo)

        if tarefa_procurada:
            return 'Tarefa já existente!'

        with open('tarefas.csv') as arquivo_leitura:
            conteudo_leitor = list(csv.reader(
                arquivo_leitura, delimiter=';', lineterminator='\n'))

        with open('tarefas.csv', 'w') as arquivo:
            escritor = csv.writer(arquivo, delimiter=';', lineterminator='\n')
            escritor.writerows(conteudo_leitor)
            escritor.writerow([titulo, data, 'Pendente'])

        return f'Tarefa {titulo} adicionada com sucesso!'

    def alterar_status_tarefa(self, titulo):
        tarefa_procurada = self._procurar_tarefa(titulo)

        if tarefa_procurada:
            with open('tarefas.csv') as arquivo_leitura:
                leitor = list(csv.reader(arquivo_leitura,
                              delimiter=';', lineterminator='\n'))
                for linha in leitor:
                    if linha[0].strip().lower() == titulo.strip().lower():
                        if linha[2] == 'Pendente':
                            linha[2] = 'Concluída'
                            novo_status = 'Concluída'
                        else:
                            linha[2] = 'Pendente'
                            novo_status = 'Pendente'
            with open('tarefas.csv', 'w') as arquivo_escrita:
                escritor = csv.writer(
                    arquivo_escrita, delimiter=';', lineterminator='\n')
                escritor.writerows(leitor)
            return f'Status da Tarefa {tarefa_procurada} atualizado para **{novo_status}**!'
        return 'Tarefa não encontrada'

    def remover_tarefa(self, titulo):
        tarefa_procurada = self._procurar_tarefa(titulo)

        if tarefa_procurada:
            with open('tarefas.csv') as arquivo_leitura:
                leitor = list(csv.reader(arquivo_leitura,
                              delimiter=';', lineterminator='\n'))
            with open('tarefas.csv', 'w') as arquivo_escrita:
                escritor = csv.writer(
                    arquivo_escrita, delimiter=';', lineterminator='\n')
                for linha in leitor:
                    if linha[0].strip().lower() != titulo.strip().lower():
                        escritor.writerow(linha)
            return f'A Tarefa {tarefa_procurada} foi removida!'
        return 'Tarefa não encontrada'

    def visualizar_tarefas(self, data):
        tarefas_dia = []
        with open('tarefas.csv') as arquivo_leitura:
            leitor = list(csv.reader(arquivo_leitura,
                          delimiter=';', lineterminator='\n'))
            for linha in leitor:
                if linha[1].strip() == data.strip():
                    tarefas_dia.append(linha)
        return tarefas_dia
