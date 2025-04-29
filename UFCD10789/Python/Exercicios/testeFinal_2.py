# Teste Final 2: Elabore uma base de dados de clientes de uma fábrica de materiais. 
# O programa deverá possibilitar inserção e listagem dos clientes bem como as compras por eles efetuadas
# ( Númcli(Automático), NomCli, morada, tel, nif, compra, Divfin ). 
# Divida final=compra – desconto, valor do desconto se compra for entre 100 e 200 é 5%, se for superior a 200 e inferior a 500 
# é 10% se superior a 500 é 15%. 
# O programa deve validar todas as entradas e na listagem deve parar cliente a cliente e ser possível busca direta por número de cliente. 
# O programa deve conter (Estruturas 3v, funções .5v, Vetores .4v, apontadores .3v). 2 H

clientes = []
numCli_count = 1

def calcular_desconto(compra):
    if 100 <= compra <= 200:
        return compra * 0.05
    elif 200 < compra < 500:
        return compra * 0.10
    elif compra >= 500:
        return compra * 0.15
    return 0

while True:
    print("\n----- MENU PRINCIPAL -----")
    print("[1] Inserir Cliente")
    print("[2] Mostrar Clientes")
    print("[3] Procurar Cliente por Número")
    print("[4] Sair")
    escolha = input("Opcao ->")

    if escolha == "1":
        print("\n--- Inserir Novo Cliente ---")
        nome = input("Nome -> ").strip()
        morada = input("Morada -> ").strip()
        telefone = input("Telefone -> ").strip()

        nif_valido = False
        while not nif_valido:
            try:
                nif = int(input("NIF (9 dígitos) -> "))
                if nif >= 100000000 and nif <= 999999999:
                    nif_valido = True
                else:
                    print("!! NIF inválido !!")
            except ValueError:
                print("!! Entrada inválida !!")

        compra_valida = False
        while not compra_valida:
            try:
                valorCompra = float(input("Valor da Compra -> "))
                if valorCompra >= 0:
                    compra_valida = True
                else:
                    print("!! O valor tem de ser positivo !!")
            except ValueError:
                print("!! Entrada inválida !!")

        desconto = calcular_desconto(valorCompra)

        divida = valorCompra - desconto

        cliente = {
            "numcli": numCli_count,
            "nome": nome,
            "morada": morada,
            "telefone": telefone,
            "nif": nif,
            "valorCompra": valorCompra,
            "desconto": desconto,
            "divida": divida
        }

        clientes.append(cliente)
        print(f"\n-- Cliente adicionado! [Nº Cliente -> {numCli_count}]")
        numCli_count += 1

    elif escolha == "2":
        print("\n----- Lista de Clientes -----")
        for cliente in clientes:
            print(f"\n-- Num. Cliente: {cliente['numcli']} --")
            print(f"-- Nome: {cliente['nome']}")
            print(f"-- Morada: {cliente['morada']}")
            print(f"-- Telefone: {cliente['telefone']}")
            print(f"-- NIF: {cliente['nif']}")
            print(f"-- Compra: {cliente['valorCompra']:.2f}€")
            print(f"-- Desconto: {cliente['desconto']:.2f}€")
            print(f"-- Dívida Final: {cliente['divida']:.2f}€")
            cont = input("\nMostrar próximo? (s/n) ->").lower()
            if cont != 's':
                break

    elif escolha == "3":
        print("\n--- Procurar Cliente ---")
        encontrado = False
        try:
            num_busca = int(input("Insira o número do cliente: "))
            for cliente in clientes:
                if cliente["numcli"] == num_busca:
                    print(f"\n-- Nome: {cliente['nome']}")
                    print(f"-- Morada: {cliente['morada']}")
                    print(f"-- Telefone: {cliente['telefone']}")
                    print(f"-- NIF: {cliente['nif']}")
                    print(f"-- Valor da Compra: {cliente['valorCompra']:.2f}€")
                    print(f"-- Desconto: {cliente['desconto']:.2f}€")
                    print(f"-- Dívida Final: {cliente['divida']:.2f}€")
                    encontrado = True
                    break
            if not encontrado:
                print("!! Cliente não encontrado !!")
        except ValueError:
            print("!! Número inválido !!")

    elif escolha == "4":
        print("-- Programa terminado")
        break

    else:
        print("!! Opção inválida !!")