#Requisitos
#1- Cadastro de Cliente
#2- Disponibilidade de horário e data
#3- Agendamento de serviço
#4- Tipos de serviços
#5- Notificação para o cliente de horário disponível, após o cancelamento de agendamento
#6- Cadastro de Barbeiro
#7- Acompanhamento de faturamento
import datetime
#Tabela de serviços e valores
Servicos = {
    "1": {"nome": "Corte Simples", "preco": 25.00},
    "2": {"nome": "Corte + Barba", "preco": 35.00},
    "3": {"nome": "Barba Completa", "preco": 20.00},
    "4": {"nome": "Corte Social", "preco": 30.00}
}
#Nome dos barbeiros e seus dias da semana de trabalho
Barbeiros = {
    "1": {"nome": "João", "dias_trabalho": ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]},
    "2": {"nome": "Carlos", "dias_trabalho": ["Terça", "Quarta", "Quinta", "Sexta"]},
    "3": {"nome": "Miguel", "dias_trabalho": ["Sábado", "Domingo"]}
}


agendamento_id_counter = 1

agendamentos = {}
clientes = {}
faturamento_barbeiros = {
    
    "João": 0.0,
    "Carlos": 0.0,
    "Miguel": 0.0
}

def mostrar_menu():
    print("\n--- Barbearia ---")
    print("1. Agendar um serviço")
    print("2. Visualizar serviços e preços")
    print("3. Visualizar barbeiros disponíveis")
    print("4. Visualizar faturamento de barbeiros")
    print("5. Sair do aplicativo")

#Reconhece o que a pessoa escreveu de acordo com o horário cada barbeiro
def obter_dia_da_semana(data_str):
    try:
        data_obj = datetime.datetime.strptime(data_str, "%Y-%m-%d")
        dias_da_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
        return dias_da_semana[data_obj.weekday()]
    except ValueError:
        return None

#agendamento do corte, e salvamento de agendamento utilizando id, escolha de serviço (se o nome bate com o barberio e dia da semana.)
def agendar_servico():
    global agendamento_id_counter

    print("\n--- Agendar Serviço ---")
#Registro do cliente
    cliente_nome = input("Digite seu nome: ")
    cliente_contato = input("Digite seu telefone/email para o lembrete: ")
#Busca os barbeiros e pede uma escolha de barbeiro, analisando se o numero do barbeiro existe
    print("Barbeiros:")
    for id_b, barbeiro in Barbeiros.items():
        print(f"{id_b}. {barbeiro['nome']}")
    barbeiro_id = input("Escolha o número do barbeiro: ")

    if barbeiro_id not in Barbeiros:
        print("Barbeiro não encontrado. Por favor, tente novamente.")
        return

    barbeiro_nome = Barbeiros[barbeiro_id]["nome"]
#Busca o barbeiro se o horário do barbeiro bate com o pedido, se não pede para refazer e diz que o barbeiro não tem esse horário.
    data = input("Digite a data (ex: 2025-05-15): ")

    dia_da_semana = obter_dia_da_semana(data)
    if not dia_da_semana:
        print("Formato de data inválido. Por favor, use YYYY-MM-DD.")
        return

    if dia_da_semana not in BARBEIROS[barbeiro_id]["dias_trabalho"]:
        print(f"{barbeiro_nome} não trabalha em {dia_da_semana}. Por favor, escolha outro dia ou barbeiro.")
        return

    hora = input("Digite a hora (ex: 14:30): ")
#Escolha de serviço
    print("\nServiços:")
    for id_s, servico in Servicos.items():
        print(f"{id_s}. {servico['nome']} (R${servico['preco']:.2f})")
    servico_id = input("Escolha o número do serviço: ")

    if servico_id not in Servicos:
        print("Serviço não encontrado. Por favor, tente novamente.")
        return

    agendamento_id = agendamento_id_counter
    agendamentos[agendamento_id] = {
        "cliente_nome": cliente_nome,
        "cliente_contato": cliente_contato,
        "barbeiro_id": barbeiro_id,
        "servico_id": servico_id,
        "data": data,
        "hora": hora
    }
    agendamento_id_counter += 1

    servico_preco = Servicos[servico_id]["preco"]
    faturamento_barbeiros[barbeiro_nome] += servico_preco

    if cliente_nome not in clientes:
        clientes[cliente_nome] = {"contato": cliente_contato, "historico": []}

    clientes[cliente_nome]["historico"].append({
        "data": data,
        "servico": SERVICOS[servico_id]["nome"],
        "barbeiro": barbeiro_nome
    })

    print("\nAgendamento realizado com sucesso!")
    print(f"Detalhes do agendamento:")
    print(f"Barbeiro: {barbeiro_nome}")
    print(f"Serviço: {Servicos[servico_id]['nome']}")
    print(f"Data e Hora: {data} às {hora}")
    print("\nUm lembrete será enviado 24h antes!")

#Consulta tabela de serviços e preços(Para mostrar para o cliente)
def mostrar_servicos():
    print("\n--- Serviços e Preços ---")
    for servico in Servicos.values():
        print(f"- {servico['nome']}: R${servico['preco']:.2f}")

#Mostra os barbeiros e seus respectivos horários(Para mostrar para o cliente)
def mostrar_barbeiros():
    print("\n--- Barbeiros ---")
    for barbeiro in Barbeiros.values():
        dias = ", ".join(barbeiro["dias_trabalho"])
        print(f"- {barbeiro['nome']}: Trabalha de {dias}")

#Busca o faturamento de cada funcionário e mostra na tela(Parte do barbeiro)
def mostrar_faturamento():
    print("\n--- Faturamento de Barbeiros ---")
    for nome, valor in faturamento_barbeiros.items():
        print(f"{nome}: R${valor:.2f}")


def rodar_aplicativo():
    while True:
        mostrar_menu()
        escolha = input("Digite sua opção: ")

        if escolha == "1":
            agendar_servico()
        elif escolha == "2":
            mostrar_servicos()
        elif escolha == "3":
            mostrar_barbeiros()
        elif escolha == "4":
            mostrar_faturamento()
        elif escolha == "5":
            print("Obrigado por usar o sistema de Barbearia. Até mais.")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")


if __name__ == "__main__":
    rodar_aplicativo()