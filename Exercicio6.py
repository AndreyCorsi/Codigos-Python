# 1- Visualização de serviços
# 2- Registro dos reparos
# 3- Alteração de status do reparo
# 4- Verificação de status do reparo
# 5- Venda de peça do estoque
# 6- Gerador de relatório de reparos
# Dicionário de serviços disponíveis com preço
servicos_oferecidos = {
    "formatação": 80,
    "limpeza completa": 50,
    "eliminação de vírus": 60,
    "instalação de software": 40
}

# Estoque de peças
pecas_estoque = {
    "RAM": 10,
    "HD": 5,
    "SSD": 7,
    "Fonte": 4,
    "Placa de vídeo": 3
}

# Lista de reparos realizados
registro_reparos = []

def mostrar_servicos():
    print("\n--- Serviços Disponíveis ---")
    for servico, preco in servicos_oferecidos.items():
        print(f"{servico} - R$ {preco}")
    print("----------------------------")

def registrar_reparo():
    cliente = input("Nome do cliente: ")
    descricao = input("Descrição do serviço (ex: formatação, troca de SSD): ")
    preco = float(input("Preço do serviço (R$): "))
    tecnico = input("Técnico responsável: ")
    
    reparo = {
        "cliente": cliente,
        "descricao": descricao,
        "preco": preco,
        "tecnico": tecnico,
        "status": "em análise"
    }
    registro_reparos.append(reparo)
    print(f"\n[OK] Reparo registrado para {cliente}.")
#Alteração de status de acordo com o andamento
def alterar_status_reparo():
    cliente = input("Nome do cliente: ")
    novo_status = input("Novo status (ex: em manutenção, finalizado): ")
    
    for r in registro_reparos:
        if r["cliente"] == cliente:
            r["status"] = novo_status
            print(f"[OK] Status do reparo atualizado para '{novo_status}'.")
            return
    print("[ERRO] Cliente não encontrado.")
#Verificar o status do reparo, para ver como está indo
def verificar_status():
    cliente = input("Nome do cliente: ")
    
    for r in registro_reparos:
        if r["cliente"] == cliente:
            print(f"O reparo de {cliente} está: {r['status']}")
            return
    print("[ERRO] Cliente não encontrado.")
#Venda das peças 
def vender_peca_estoque():
    peca = input("Nome da peça: ")
    qtd = int(input("Quantidade a vender: "))
    
    if peca in pecas_estoque:
        if pecas_estoque[peca] >= qtd:
            pecas_estoque[peca] -= qtd
            print(f"[OK] {qtd}x {peca} vendida(s). Restam {pecas_estoque[peca]}.")
            if pecas_estoque[peca] <= 2:
                print(">>> Atenção: estoque baixo, providencie reposição!")
        else:
            print("[ERRO] Quantidade solicitada maior que o estoque.")
    else:
        print("[ERRO] Peça não encontrada no estoque.")
#Para gerar o relatorio
def gerar_relatorio_reparos():
    print("\n--- Relatório Geral ---")
    print(f"Total de reparos: {len(registro_reparos)}")
    
    tecnicos = {}
    for r in registro_reparos:
        t = r["tecnico"]
        tecnicos[t] = tecnicos.get(t, 0) + 1

    print("Serviços por técnico:")
    for t, qtd in tecnicos.items():
        print(f" - {t}: {qtd} serviço(s)")
    print("------------------------")

def menu_principal():
    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("1. Mostrar serviços")
        print("2. Registrar reparo")
        print("3. Alterar status do reparo")
        print("4. Verificar status do reparo")
        print("5. Vender peça do estoque")
        print("6. Gerar relatório de reparos")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            mostrar_servicos()
        elif opcao == "2":
            registrar_reparo()
        elif opcao == "3":
            alterar_status_reparo()
        elif opcao == "4":
            verificar_status()
        elif opcao == "5":
            vender_peca_estoque()
        elif opcao == "6":
            gerar_relatorio_reparos()
        elif opcao == "0":
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("[ERRO] Opção inválida, tente novamente.")

menu_principal()