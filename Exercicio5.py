#Requisitos
#1- Cadastro de Cliente
#2- Disponibilidade de horário e data
#3- Agendamento de serviço
#4- Tipos de serviços
#5- Confirmação de agendamento
#6- Confirmação de Presença
#7- Notificação para o cliente de horário disponível, após o cancelamento de agendamento
#8- Cadastro de Barbeiro
#9- Visualização de Agendamentos feitos
#10- Acompanhamento de faturamento
import datetime

SERVICOS = {
    "1": {"nome": "Corte Simples", "preco": 25.00},
    "2": {"nome": "Corte + Barba", "preco": 35.00},
    "3": {"nome": "Barba Completa", "preco": 20.00},
    "4": {"nome": "Corte Social", "preco": 30.00}
}

BARBEIROS = {
    "1": {"nome": "João", "dias_trabalho": ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]},
    "2": {"nome": "Carlos", "dias_trabalho": ["Terça", "Quarta", "Quinta", "Sexta"]},
    "3": {"nome": "Miguel", "dias_trabalho": ["Sábado", "Domingo"]}
}

agendamentos = {}
clientes = {}
faturamento_barbeiros = {
    "João": 0.0,
    "Carlos": 0.0,
    "Miguel": 0.0
}
agendamento_id_counter = 1


def mostrar_menu():
    print("\n--- BARBEARIA DO JOE ---")
    print("1. Agendar um serviço")
    print("2. Ver serviços e preços")
    print("3. Ver barbeiros disponíveis")
    print("4. Ver faturamento de barbeiros")
    print("5. Sair do aplicativo")


def obter_dia_da_semana(data_str):
    try:
        data_obj = datetime.datetime.strptime(data_str, "%Y-%m-%d")
        dias_da_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
        return dias_da_semana[data_obj.weekday()]
    except ValueError:
        return None


def agendar_servico():
    global agendamento_id_counter

    print("\n--- Agendar Serviço ---")

    cliente_nome = input("Digite seu nome: ")
    cliente_contato = input("Digite seu telefone/email para o lembrete: ")

    print("Barbeiros:")
    for id_b, barbeiro in BARBEIROS.items():
        print(f"{id_b}. {barbeiro['nome']}")
    barbeiro_id = input("Escolha o número do barbeiro: ")

    if barbeiro_id not in BARBEIROS:
        print("Barbeiro não encontrado. Por favor, tente novamente.")
        return

    barbeiro_nome = BARBEIROS[barbeiro_id]["nome"]

    data = input("Digite a data (ex: 2025-05-15): ")

    dia_da_semana = obter_dia_da_semana(data)
    if not dia_da_semana:
        print("Formato de data inválido. Por favor, use YYYY-MM-DD.")
        return

    if dia_da_semana not in BARBEIROS[barbeiro_id]["dias_trabalho"]:
        print(f"{barbeiro_nome} não trabalha em {dia_da_semana}. Por favor, escolha outro dia ou barbeiro.")
        return

    hora = input("Digite a hora (ex: 14:30): ")

    print("\nServiços:")
    for id_s, servico in SERVICOS.items():
        print(f"{id_s}. {servico['nome']} (R${servico['preco']:.2f})")
    servico_id = input("Escolha o número do serviço: ")

    if servico_id not in SERVICOS:
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

    servico_preco = SERVICOS[servico_id]["preco"]
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
    print(f"Serviço: {SERVICOS[servico_id]['nome']}")
    print(f"Data e Hora: {data} às {hora}")
    print("\nUm lembrete será enviado 24h antes!")


def mostrar_servicos():
    print("\n--- Serviços e Preços ---")
    for servico in SERVICOS.values():
        print(f"- {servico['nome']}: R${servico['preco']:.2f}")


def mostrar_barbeiros():
    print("\n--- Barbeiros ---")
    for barbeiro in BARBEIROS.values():
        dias = ", ".join(barbeiro["dias_trabalho"])
        print(f"- {barbeiro['nome']}: Trabalha de {dias}")


def mostrar_faturamento():
    print("\n--- Faturamento de Barbeiros (Mês) ---")
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
            print("Obrigado por usar o sistema da Barbearia do Joe! Até mais.")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")


if __name__ == "__main__":

    rodar_aplicativo()

