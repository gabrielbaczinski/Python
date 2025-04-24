senha = 1234
saldo_atual = 0
passagem = 6.00
passagem_reserva = 6.00
contador = 2
acesso = True
confirma_senha = 0
domingo = False
tarifa_domingo = passagem * 0.5
while acesso == True:
    usuario = int(input('Qual é o seu cartão de acesso?\n'
                        '[1] - Usuário\n'
                        '[2] - Administrador\n'
                        '[3] - Sair\n'))
    menu1, menu2 = True, True
    if usuario == 1:
        while menu1 == True:
            menu_usuario = int(input('Seja bem-vindo, usuário!\n'
                                     'O que deseja fazer?\n'
                                     '[1] - Recarregar Cartão\n'
                                     '[2] - Usar Cartão\n'
                                     '[3] - Voltar\n'))
            if menu_usuario == 1:
                saldo_recarga = float(input('Quantos créditos gostaria de recarregar?\n'))
                saldo_atual += saldo_recarga
                print(f'Novo saldo: {saldo_atual:.2f} créditos\n')
            elif menu_usuario == 2:
                if saldo_atual < passagem:
                    print('Você não possui saldo suficiente para essa transação\n')
                else:
                    print(f'Novo saldo {saldo_atual - passagem:.2f} créditos.\n')
                    saldo_atual = saldo_atual - passagem
            elif menu_usuario == 3:
                menu1 = False
            else:
                print(f'Opção inválida. Tente novamente.\n')
    elif usuario == 2:
        if contador == 0:
            print('Tentativas excedidas, tente novamente mais tarde.\n')
            continue
        confirma_senha = int(input('Por favor, digite sua senha.\n'))
        while senha != confirma_senha:
            if contador > 0:
                print(f'Senha incorreta. {contador} tentativas restantes.\n')
                confirma_senha = int(input('Por favor, digite sua senha novamente.\n'))
                if senha == confirma_senha:
                    contador = 2
                contador = contador - 1
            elif contador == 0:
                print('Tentativas excedidas, tente novamente mais tarde.\n')
                break
        if confirma_senha == senha:
            contador = 2
            while menu2 == True:
                menu_adm = int(input('Seja bem-vindo, administrador!\n'
                                     'O que deseja fazer?\n'
                                     '[1] - Visualizar Créditos\n'
                                     '[2] - Alterar o Valor da Passagem\n'
                                     '[3] - Tarifa de Domingo\n'
                                     '[4] - Voltar\n'))
                if menu_adm == 1:
                    print(f'O cartão possui {saldo_atual:.2f} créditos.\n')

                elif menu_adm == 2:
                    if domingo == False:
                        passagem = float(input('Qual o novo valor da passagem?\n'))
                        print(f'O valor da passagem foi definido para {passagem:.2f}\n')
                        passagem_reserva = passagem
                        tarifa_domingo = passagem * 0.5
                        print(f'Se hoje fosse domingo, a passagem seria {tarifa_domingo:.2f}\n')
                    else:
                        passagem = float(input('Qual o novo valor da passagem?\n'))
                        print(f'O valor da passagem foi definido para {passagem:.2f}\n')
                        passagem_reserva = passagem
                        tarifa_domingo = passagem * 0.5
                        passagem = tarifa_domingo
                        print(f'Como hoje é domingo, a passagem será {passagem:.2f}\n')
                elif menu_adm == 3:
                    if domingo == False:
                        domingo = True
                        passagem = tarifa_domingo
                        print('Tarifa de Domingo Ativada.\n')
                    else:
                        domingo = False
                        passagem = passagem_reserva
                        print('Tarifa de Domingo Desativada.\n')
                elif menu_adm == 4:
                    menu2 = False
                else:
                    print(f'Opção inválida. Tente novamente.\n')
    elif usuario == 3:
        acesso = False
    else:
        print('Opção Inválida. Tente novamente.\n')

