# Alunos: Gabriel Baczinski Santana, João Guilherme Marques Camargo

import json
import getpass

USUARIOS_JSON = "usuarios.json"
PERMISSOES_JSON = "permissoes.json"

def carrega_usuarios():
    try:
        with open(USUARIOS_JSON, mode="r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []  
    
def salva_usuarios(usuarios):
    try:
        with open(USUARIOS_JSON, mode="w", encoding="utf-8") as arquivo:
            json.dump(usuarios, arquivo, indent=4)
            print("Usuário salvo com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar usuário: {e}")

def carrega_permissoes():
    try:
        with open(PERMISSOES_JSON, mode="r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def tem_permissao(usuario, arquivo, acao):
    permissoes = carrega_permissoes()
    if arquivo in permissoes:
        permissoes_usuario = permissoes[arquivo].get(usuario, [])
        return acao in permissoes_usuario
    return False 

def listar_arquivos():
    permissoes = carrega_permissoes()
    arquivos_disponiveis = list(permissoes.keys())
    print("\nArquivos disponíveis:")
    for i, arquivo in enumerate(arquivos_disponiveis, 1):
        print(f"[{i}]{arquivo}")
    return arquivos_disponiveis


def selecionar_arquivo():
    arquivos = listar_arquivos()
    while True:
        try:
            opcao = int(input("\nDigite o número do arquivo desejado: ")) - 1
            if 0 <= opcao < len(arquivos):
                return arquivos[opcao]
            else:
                print("Opção inválida.")
        except ValueError:
            print("Digite um número.")
            
def cadastro():
    usuarios = carrega_usuarios()
    permissoes = carrega_permissoes()
    email = input('Digite o e-mail: ')
    senha = getpass.getpass(prompt='Digite a senha:')
    for usuario in usuarios:
        if usuario["email"] == email:
            print("E-mail já cadastrado.")
            return
    novo_usuario = {"email": email, "senha": senha}
    usuarios.append(novo_usuario)
    for arquivo in permissoes.keys():
        if email not in permissoes[arquivo]:  
            permissoes[arquivo][email] = [] 
    salva_usuarios(usuarios)
    salva_permissoes(permissoes)
    print(f'Usuário {email} cadastrado com sucesso!')
    menu(email)
    
def salva_permissoes(permissoes):
    try:
        with open(PERMISSOES_JSON, mode="w", encoding="utf-8") as arquivo:
            json.dump(permissoes, arquivo, indent=4)
            print("Permissões salvas com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar permissões: {e}")


def login():
    tentativas = 5
    usuarios = carrega_usuarios()
    while tentativas > 0:
        user = input('Digite o e-mail: ')
        password = getpass.getpass(prompt='Digite a senha: ')
        for usuario in usuarios:
            if usuario["email"] == user and usuario["senha"] == password:
                print(f'Login realizado com sucesso!\nBem-vindo, {user}!')
                menu(user)
                return
        tentativas -= 1
        print(f'Credenciais inválidas. {tentativas} tentativas restantes.')
    if tentativas == 0:
        print("Número máximo de tentativas atingidas.")
    

def menu(usuario):
    while True:
        print('\nBem-vindo ao Menu Principal!\n'
              '[1] - Listar arquivos\n'
              '[2] - Criar arquivo\n'
              '[3] - Ler arquivo\n'
              '[4] - Excluir arquivo\n'
              '[5] - Executar arquivo\n'
              '[6] - Sair\n')
        opcao = input('Digite a opção desejada: ')
        if opcao == '1':
            listar_arquivos()  
        elif opcao in ['2', '3', '4', '5']:
            acoes = {'2': 'criar', '3': 'ler', '4': 'excluir', '5': 'executar'}
            acao = acoes[opcao]
            arquivo = selecionar_arquivo()
            if arquivo:
                if tem_permissao(usuario, arquivo, acao):
                    print(f"Acesso permitido para {acao} o arquivo {arquivo}.")
                else:
                    print(f"Acesso negado para {acao} o arquivo {arquivo}.")
        elif opcao == '6':
            print("Obrigado!")
            break  
        else:
            print("Opção inválida.")

while True:
    print('\nBem-vindo!\n'
          '[1] - Cadastro\n'
          '[2] - Login\n'
          '[3] - Sair\n')
    opcaoMenu = input('Digite a opção desejada: ')
    if opcaoMenu == '1':
        cadastro()
    elif opcaoMenu == '2':
        login()
    elif opcaoMenu == '3':
        print('Valeu tamo junto gratidão e fé!\n')
        break
    else:
        print("Opção inválida.")
