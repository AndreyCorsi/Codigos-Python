#exercicio2
#cadastrar paciente
#remover paciente
#mostrar pacientes cadastrados

def menu():
    print("\n--- Sistema Hospitalar ---")
    print("1 - Cadastrar Paciente")
    print("2 - Consultar Pacientes")
    print("3 - Atender pacientes")
    print("4 - Sair")
    return input("Escolha uma opção: ")

paciente = []

while True:
    
    opcao = menu()
    
    if opcao == "1":
       paciente.append(input("Qual nome do paciente: "))
       print("Paciente Cadastrado com sucesso!")
       
    elif opcao == "2":
        if paciente == []:
            print("Não a pacientes na Lista!")
        else:
            print(f"paciente: {paciente}")
            
    elif opcao == "3":
        if len (paciente) == 0:
            print("Não a pacientes para atender!")
        else:
            paciente.pop()
            print(f"Lista de pacientes a ser atendidos{paciente}: ")
    
    elif opcao == "4":
            print("Saindo do sistema... até mais")
            break
    
    else:

        print("Opção Invalida! Tente Novamente")
