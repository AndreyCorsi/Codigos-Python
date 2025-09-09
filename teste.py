#Criar usuario com nome, email e senha
#Verificar usuario com base no email
#Fazer login

from dataclasses import dataclass

@dataclass
class Usuario:
    nome: str
    email: str
    senha: str

def criar_usuario():
    print("criar usuario")
    nome = input("Digite o nome: ")
    email = input("Digite o email: ")
    senha = input("Digite sua senha: ")
    usuario_digitado = Usuario(nome,email,senha)
    lista.append(usuario_digitado)
    print ("Usuario Cadastrado com sucesso!")
def pesquisar_email():
    print ("Pesquisar Email")
    login_email = input("Insira seu email: ")
    login_senha = input("Insira sua senha: ")
        
    for usuario in lista:
        if usuario.email == login_email:
                if usuario.senha == login_senha:
                    print("Acesso autorizado!")
                else:
                    print("Email ou senha incorreto")
        else:
                print("Email ou senha incorreto")
def fazendo_login():
    print("Fazendo login...")
    nome_digitado = input("Qual seu nome: ")
    for usuario in lista:
        if usuario.nome == nome_digitado:
                print(f"email desse usuario -> {usuario.email}")

def menu():
    print("--- intagram ---")
    print("1 - Cadastrar ")
    print("2 - Login ")
    print("3 - Pesquisar Usuario ")
    print("4 - Sair")
    return input("\nEscolha uma opção: ")
    
lista = []

while True:
    
    opcao = menu()
        
    if opcao == "1":
            criar_usuario()
    elif opcao == "2":
            pesquisar_email()
    elif opcao == "3":
            fazendo_login()
    elif opcao == "4":
        print("Até logo")
        break