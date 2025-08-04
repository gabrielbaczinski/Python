import hashlib
import csv
import getpass
import os

# Usando diretório atual para garantir criação dos arquivos
base_dir = os.path.dirname(os.path.abspath(__file__))  # pega a pasta onde o .py está
os.makedirs(base_dir, exist_ok=True)  # cria a pasta se não existir
dadosUsuarios = os.path.join(base_dir, 'usuarios.csv')
usuariosBanidos = os.path.join(base_dir, 'bloqueados.csv')
falhasLogin = {}

def aplicarHash(textoPlano):
    return hashlib.sha256(textoPlano.encode()).hexdigest()

def criarArquivoUsuariosSeNaoExistir():
    if not os.path.exists(dadosUsuarios):
        with open(dadosUsuarios, 'w', newline='', encoding='utf-8') as f:
            escritor = csv.writer(f)
            escritor.writerow(['usuario', 'senhaHash'])

def incluirNovoUsuario():
    criarArquivoUsuariosSeNaoExistir()

    nomeEntrada = input('Informe o nome (até 4 caracteres): ')[:4]
    senhaEntrada = getpass.getpass('Informe a senha (até 4 caracteres): ')[:4]
    senhaProtegida = aplicarHash(senhaEntrada)

    with open(dadosUsuarios, 'a', newline='', encoding='utf-8') as planilha:
        gravar = csv.writer(planilha)
        gravar.writerow([nomeEntrada, senhaProtegida])

    print('Cadastrado com sucesso!\n')

def estaSuspenso(nomeUsuario):
    if not os.path.exists(usuariosBanidos):
        return False
    with open(usuariosBanidos, 'r', encoding='utf-8') as arquivo:
        bloqueados = [linha.strip() for linha in arquivo]
        return nomeUsuario in bloqueados

def registrarSuspensao(usuarioAlvo):
    with open(usuariosBanidos, 'a', encoding='utf-8') as arquivo:
        arquivo.write(f'{usuarioAlvo}\n')

def loginUsuario():
    if not os.path.isfile(dadosUsuarios):
        print('Nenhum usuário cadastrado ainda.\n')
        return

    nomeDigitado = input('Usuário (até 4 caracteres): ')[:4]

    if estaSuspenso(nomeDigitado):
        print('Conta suspensa.\n')
        return

    senhaDigitada = getpass.getpass('Senha (até 4 caracteres): ')[:4]
    verificador = aplicarHash(senhaDigitada)

    acessoPermitido = False

    with open(dadosUsuarios, 'r', encoding='utf-8') as base:
        leitor = csv.reader(base)
        next(leitor)  # pula o cabeçalho
        for linha in leitor:
            nomeRegistro, senhaRegistro = linha
            if nomeDigitado == nomeRegistro and verificador == senhaRegistro:
                acessoPermitido = True
                break

    if acessoPermitido:
        print(f'Login efetuado com sucesso, {nomeDigitado}!\n')
        falhasLogin[nomeDigitado] = 0
    else:
        falhasLogin[nomeDigitado] = falhasLogin.get(nomeDigitado, 0) + 1
        print('Credenciais incorretas.\n')
        if falhasLogin[nomeDigitado] >= 4:
            print('Tentativas excedidas. Conta será suspensa.\n')
            registrarSuspensao(nomeDigitado)

def iniciarSistema():
    while True:
        print('Cripto Hash System')
        print('1 - Cadastre-se')
        print('2 - Login')
        print('3 - Sair')
        escolha = input('Opção: ')

        if escolha == '1':
            incluirNovoUsuario()
        elif escolha == '2':
            loginUsuario()
        elif escolha == '3':
            print('Saindo do sistema.')
            break
        else:
            print('Opção incorreta.\n')

if __name__ == '__main__':
    iniciarSistema()
