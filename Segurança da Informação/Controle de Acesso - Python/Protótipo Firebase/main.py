import pyrebase


firebaseConfig = {
  "apiKey": "AIzaSyAScLa1Qp3Qcbdc1hNh1lkacSSY7yUNcXM",
  "authDomain": "bsi-seginfo-f28aa.firebaseapp.com",
  "projectId": "bsi-seginfo-f28aa",
  "storageBucket": "bsi-seginfo-f28aa.firebasestorage.app",
  "messagingSenderId": "937035139085",
  "appId": "1:937035139085:web:5942a435bf796c54052d44",
  "databaseURL": ""
};

APP = pyrebase.initialize_app(firebaseConfig)

AUTH = APP.auth() 

def criar_usuario():
    try:
        email = str(input('Digite o e-mail: '))
        senha = str(input('Digite a senha: '))
        AUTH.create_user_with_email_and_password(email, senha)
        token = AUTH.get_account_info(email, senha)
        print(token)
    except Exception as e:
        print(f"An error occurred: {e}")

def verificar_email(email, senha, token):
    AUTH.sign_in_with_email_and_password(email, senha)
    print(AUTH.get_account_info(token['idToken']))
    
def redefinir_senha(email):
    AUTH.send_password_reset_email(email)
    
def menu():
    print('1. Criar usuário')
    print('2. Verificar e-mail')
    print('3. Redefinir senha')
    options = {1 : criar_usuario, 2 : verificar_email, 3 : redefinir_senha}
    opcao = int(input('Digite a opção desejada: '))
    
    if opcao == 1:
        options[opcao]()
    elif opcao == 2:
        options[opcao]()
    elif opcao == 3:
        options[opcao]()
    else:
        print('Opção inválida. Tente novamente.')
        
    
menu()
# 1. Criar dois users no firebase
#    1. Solicitar info pelo terminal
# 2. Verificar e-mail dos usuários
# 3. Redefinir senha dos usuários
# 4. Bloquear usuário após 5 tentativas de login
