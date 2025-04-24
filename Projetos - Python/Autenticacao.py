import getpass
import csv

usuario = 'gabriel'
senha = '123456'

usuario_input = input('Digite o usuário: ')
senha_input = getpass.getpass(prompt='Digite a senha: ')

contador = 0 
usuarios_bloqueados = []
senhas_bloqueadas = []

while contador < 4:
    if usuario == usuario_input and senha == senha_input:
        print(f'Seja bem vindo, {usuario_input}!')
        with open('senha.csv', 'w', newline='') as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow(['Senha:'])  
            escritor.writerow([senha]) 
        break
    elif usuario == usuario_input or senha != senha_input:
        print('Login ou senha incorreto. Tente novamente mais tarde.')
        contador += 1
        usuario_input = input('Digite o usuário: ')
        senha_input = getpass.getpass(prompt='Digite a senha: ')
        usuarios_bloqueados.append(usuario_input)
        senhas_bloqueadas.append(senha_input)
if contador == 4:
    print('Conta bloqueada. Tente novamente mais tarde.')
    with open('UsuarioBloqueado.csv', 'w', newline='') as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow([usuarios_bloqueados]) 
            escritor.writerow([senhas_bloqueadas])
