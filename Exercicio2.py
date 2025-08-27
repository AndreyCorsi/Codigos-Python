#Sistema de Cadastro de Paciente
#1 - Cadastrar paciente
#2 - Mostrar paciente cadastrado
#3 - Atender paciente
#4 - Sair
def menu():
    print("\n---Sistema de Gerenciamento de Paciente")
    print("1 - Cadastrar paciente")
    print("2 - Mostrar paciente cadastrado")
    print("3 - Atender paciente")
    print("4 - Listar pacientes registrados")
    print("5 - Sair")
    return input("Escolha uma opção: ")
    
    paciente = [None]
    
while True:
    opcao = menu()
        
    if opcao == "1":
        paciente = input("Digite nome do paciente: ")
        print(f"Paciente {[paciente]}cadastrado com sucesso")
        
    elif opcao == "2":
        if paciente is None
            print("Nenhum paciente registrado")
        else:
            print(f"Pacientes atuais {paciente} ")
        
    
    
    
    

    
    
    
    
