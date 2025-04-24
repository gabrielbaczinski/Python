from datetime import datetime


### Biblioteca de funções

# Módulo para comprar créditos.
# Entrada: Saldo a ser carregado, inserido através do input.
# Saída: Variável global atualizada com o saldo inserido.

def comprar_credito(novo_saldo, creditos):
    return creditos + novo_saldo


# Módulo para verificar se há uma bicicleta locada.
# Entrada: Leitura do comprimento da lista.
# Saída: True caso a lista tenha dois indíces, False caso contrário.

def verificar_bicicleta_alugada(locacao):
    for aluguel in locacao:
        if len(aluguel) == 2:
            return True
    return False


# Módulo para locar uma bicicleta, com verificações de locação e saldo de créditos.
# Entrada: Recebe o valor True/False da função de verificação.
# Saída: Caso True, exibe a mensagem que a bicicleta está alugada. False, pede para o usuário preencher os inputs de locação.
# Entrada: Verifica se o saldo global dos créditos é menor que 5.
# Saída: Caso saldo seja menor que 5, exibe a mensagem que o user possui créditos insuficientes.

def locar_bicicleta(creditos, locacao):
    if verificar_bicicleta_alugada(locacao) == True:
        print('Você já possui uma Bike alugada. Devolva a Bike antes de alugar outra.\n')
        return locacao

    if creditos < 5:
        print('Créditos insuficientes. Você precisa de no mínimo 5 créditos para alugar uma Bike\n')
        return locacao

    print('Bike locada!')
    data_locacao = input('Locação - Date (DD/MM/YYYY): ')
    hora_locacao = input('Locação - Hour (HH:MM): ')
    print('Você já pode retirar sua bike, bom passeio!\n')
    locacao.append([data_locacao, hora_locacao])
    return locacao


# Módulo para listar bicicletas alugadas, printando o conteúdo da lista.
# Entrada: Faz a leitura do comprimento da lista.
# Saída: Caso comprimento maior que 2, exibe o conteúdo armazenado da lista.

def listar_bicicletas_alugadas(locacao):
    print('Bicicletas alugadas:')
    for cont in range(len(locacao)):
        aluguel = locacao[cont]
        if len(aluguel) == 2:
            print(f'{cont + 1}: {aluguel[0]} {aluguel[1]}')


# Módulo para obter os dados de devolução.
# Entrada: Recebe as informações de data/hora de devolução.
# Saída: Armazena as informações para serem lidas na função seguinte.

def obter_dados_devolucao():
    data_devolucao = input('Devolução - Date (DD/MM/YYYY): ')
    hora_devolucao = input('Devolução - Hour (HH:MM): ')
    return data_devolucao, hora_devolucao


# Módulo para realizar o cálculo do valor da locação, convertendo as informações em datas/horas válidas.
# Entrada: Recebe os valores de data/hora das variáveis de locação/devolução.
# Saída: Converte essas informações, cálcula a diferença entre elas e guarda em uma variável.

def calcular_tempo_aluguel(locacao, escolha, data_devolucao, hora_devolucao):
    horas_locacao = datetime.strptime(f"{locacao[escolha][0]} {locacao[escolha][1]}", "%d/%m/%Y %H:%M")
    horas_devolucao = datetime.strptime(f"{data_devolucao} {hora_devolucao}", "%d/%m/%Y %H:%M")
    saldo_horas = horas_devolucao - horas_locacao
    horas_alugadas = int(saldo_horas.total_seconds() // 3600)
    return horas_alugadas


# Módulo para inserir as informações de devolução na lista, e atualizar os créditos baseado no tempo de locação.
# Entrada: Inserção na lista os valores de hora/data de devolução.
# Saída: Exibe uma mensagem ao usuário e atualiza a variável global de saldo.

def atualizar_locacao_e_creditos(locacao, escolha, data_devolucao, hora_devolucao, creditos, horas_alugadas):
    locacao[escolha].append(data_devolucao)
    locacao[escolha].append(hora_devolucao)
    creditos -= horas_alugadas
    print('Devolução concluída, bom descanso!')
    print(f'Você pedalou por: {horas_alugadas:.2f} horas. Incrível!!!\n')
    return creditos, locacao


# Módulo para devolução da bicicleta, juntamente com a verificação de locação.
# Entrada: Recebe os valores da função de verificação.
# Saída: Caso False, chama a função para inserir valores de devolução, converte os valores, insere na lista e atualiza o saldo.
# Caso True, exibe a mensagem que não há nenhuma bicicleta alugada.

def devolver_bicicleta(creditos, locacao):
    if verificar_bicicleta_alugada(locacao):
        escolha = False

        data_devolucao, hora_devolucao = obter_dados_devolucao()
        horas_alugadas = calcular_tempo_aluguel(locacao, escolha, data_devolucao, hora_devolucao)
        creditos, locacao = atualizar_locacao_e_creditos(locacao, escolha, data_devolucao, hora_devolucao, creditos,
                                                         horas_alugadas)
    else:
        print('Nenhuma bicicleta está alugada.\n')

    return creditos, locacao


# Módulo para gerar o relatório de uso, printando as informações inseridas na lista.
# Entrada: Exibe o conteúdo do índice [0][1] da lista, e verifica o comprimento.
# Saída: Caso comprimento maior que dois, exibe os indíces [2][3] da lista. Caso menor, exige uma mensagem ao usuário.

def gerar_relatorio_uso(locacao):
    print('Relatório de uso:')
    for index in range(len(locacao)):
        aluguel = locacao[index]
        print(f'Bicicleta {index + 1}:')
        print(f'  - Dia: {aluguel[0]}')
        print(f'  - Retirou: {aluguel[1]} horas.')
        if len(aluguel) > 2:
            print(f'  - Dia: {aluguel[2]}')
            print(f'  - Devolveu: {aluguel[3]} horas.')
        else:
            print('  - Devolução pendente...')
    print()


# Módulo para printar e selecionar as opções do menu.
# Entrada: Recebe o seleção de função do menu.
# Saída: Faz a leitura do comando, e direciona o usuário a função correspondente.

def escolher_menu(creditos, locacao):
    while True:
        print('Menu de Opções:\n',
              '[1] - Comprar créditos\n',
              '[2] - Consultar créditos\n',
              '[3] - Locar uma bicicleta\n',
              '[4] - Devolver bicicleta\n',
              '[5] - Relatório de uso\n',
              '[6] - Sair\n')

        opcao_menu = int(input('O que deseja fazer? '))

        if opcao_menu == 1:
            novo_saldo = int(input('Quantos créditos deseja comprar? '))
            creditos = comprar_credito(novo_saldo, creditos)
            print(f'Saldo atualizado: {creditos} créditos.\n')
        elif opcao_menu == 2:
            print(f'Você possui {creditos} créditos.\n')
        elif opcao_menu == 3:
            locacao = locar_bicicleta(creditos, locacao)
        elif opcao_menu == 4:
            creditos, locacao = devolver_bicicleta(creditos, locacao)
        elif opcao_menu == 5:
            gerar_relatorio_uso(locacao)
        elif opcao_menu == 6:
            print('Obrigado pela preferência e volte sempre!\n')
            break
        else:
            print('Opção inválida\n')
    return creditos, locacao


### Script de funcionamento

# Variáveis globais
user = 'user1234'
senha = 1234
creditos = 0
contador = 2
locacao = []

# Header inicial
print(
    '\nBem-vindo ao serviço de locações de bicicletas no Python. O Bikepy!\n'
    '-----------------------------------------------------------------------'
    '\nPara iniciar a sua utilização do programa, forneça seu login e senha.\n'
)

# Loop para verificação de user.
# Entrada: Recebe a informação do user pelo input, e verifica o valor do mesmo com a variável global.
# Saída: Caso o usuário não passe pela verificação, o contador é reduzido e uma nova verificação é acionada.

confirma_user = str(input('Por favor, digite seu user: '))
while user != confirma_user:
    if contador > 0:
        print(f'User incorreto. {contador} tentativas restantes.\n')
        contador -= 1
        confirma_user = str(input('Por favor, digite seu user novamente: '))
        if confirma_user == user:
            contador = 1
    # Se o contador chegar a 0, o programa é encerrado.
    if contador == 0:
        print('Tentativas excedidas, tente novamente mais tarde.')
        break

# Loop para verificação de senha.
# Entrada: Recebe a informação da senha pelo input, e verifica o valor da mesma com a variável global.
# Saída: Caso o usuário não passe pela verificação, o contador é reduzido e uma nova verificação é acionada.

if contador > 0:
    contador = 2
    confirma_senha = int(input('Por favor, digite sua senha: '))
    while senha != confirma_senha:
        if contador > 0:
            print(f'Senha incorreta. {contador} tentativas restantes.\n')
            contador -= 1
            confirma_senha = int(input('Por favor, digite sua senha novamente: '))
            if confirma_senha == senha:
                contador = 1
        # Se o contador chegar a 0, o programa é encerrado.
        if contador == 0:
            print('Tentativas excedidas, tente novamente mais tarde.')
            break

    if contador > 0:
        creditos, locacao = escolher_menu(creditos, locacao)
