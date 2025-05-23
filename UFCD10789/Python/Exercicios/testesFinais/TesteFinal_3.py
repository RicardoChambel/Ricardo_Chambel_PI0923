""" 
Crie um programa para gerenciar os fornecedores de uma empresa de construção. O programa deve permitir:
Funcionalidades:
    Inserir os dados dos fornecedores com os seguintes campos:
        NumFor (gerado automaticamente);
        NomeFor (nome do fornecedor);
        Endereço;
        Telefone (validar se tem ao menos 9 dígitos);
        NIF (validar se tem exatamente 9 dígitos);
        ValorFornecido (valor total dos equipamentos fornecidos);
        Desconto (calculado automaticamente);
        ValorFinal = ValorFornecido - Desconto.
        Regras de desconto:
            Se o valor fornecido for entre 1.000 e 5.000 €, aplicar 8% de desconto;
            Se entre 5.001 e 10.000 €, aplicar 12%;
            Se superior a 10.000 €, aplicar 18%.
    Listar os fornecedores um por um (parando entre cada um com um Enter);
    Permitir busca direta por número do fornecedor (NumFor).

Observações:
    Todas as entradas devem ser validadas.
    O programa deve ser estruturado com funções.
    Use uma lista para armazenar os dados dos fornecedores. 
"""
fornecedoresList = []

def insertForn():
    print("\n| Construcao Banana Inc. |")
    print("- Inserir dados de fornecedor -")
    numFor=len(fornecedoresList) + 1
    # Nome
    while True:
        try:
            nome=input("| Novo Nome ->> ")
            break
        except:
            print("--!! Valor inserido invalido !!--\n")
    # Endereco
    while True:
        try:
            endereco=input("| Novo Endereco ->> ")
            break
        except:
            print("--!! Valor inserido invalido !!--\n")
    # Telefone
    while True:
        try:
            tele=int(input("| Novo Telefone [formato: 000000000] ->> "))
            if tele >= 100000000 and tele <= 999999999:
                break
            else:
                print("--!! Telefone invalido !!--\n")
        except:
            print("--!! O valor inserido não é válido !!--\n")
    # NIF
    while True:
        try:
            nif=int(input("| Novo NIF [formato: 000000000] ->> "))
            break
        except:
            print("--!! Valor inserido invalido !!--\n")
    # Valor Fornecido
    while True:
        try:
            valorFornecido=float(input("| Valor Fornecido [formato: 000.0] ->> "))
            break
        except:
            print("--!! Valor inserido invalido !!--\n")
    # Desconto
    desconto = 0
    if 1000 <= valorFornecido <= 5000:
        desconto = valorFornecido*(8/100)
        valorFinal = valorFornecido - desconto
        print(f"| Desconto aplicado: 8%")
        print(f"| Valor Final: {valorFinal}€")
    elif 5001 <= valorFornecido <= 10000:
        desconto = valorFornecido*(12/100)
        valorFinal = valorFornecido - desconto
        print(f"| Desconto aplicado: 12%")
        print(f"| Valor Final: {valorFinal}€")
    elif 10000 <= valorFornecido:
        desconto = valorFornecido*(18/100)
        valorFinal = valorFornecido - desconto
        print(f"| Desconto aplicado: 18%")
        print(f"| Valor Final: {valorFinal}€")
    else:
        valorFinal = valorFornecido
    
    novo_fornecedor = {
        "numFor":numFor,
        "nome":nome,
        "endereco":endereco,
        "telefone":tele,
        "nif":nif,
        "valorFornecido":valorFornecido,
        "valorFinal":valorFinal
        
    }
    fornecedoresList.append(novo_fornecedor)
    
    print("\n| -- Dados Do Novo Fornecedor Guardado -- |")
    print(f"| Numero de Fornecedor -> {numFor}")
    print(f"| Nome -> {nome}")
    print(f"| Endereco -> {endereco}")
    print(f"| Telefone -> {tele}")
    print(f"| NIF -> {nif}")
    print(f"| Valor Fornecido -> {valorFornecido}€")
    print(f"| Valor Final -> {valorFinal}€")
    print("| --")
    
    input("-- ENTER para voltar --")

def listaForns():
    print("\n| Construcao Banana Inc. |")
    print("- Listar fornecedores -")
    for forn in fornecedoresList:
        print(f"\n| Fornecedor nº{forn['numFor']}")
        print(f"> Nome: {forn['nome']}")
        print(f"> Endereco: {forn['endereco']}")
        print(f"> Telefone: {forn['telefone']}")
        print(f"> NIF: {forn['nif']}")
        print(f"> Valor Fornecido: {forn['valorFornecido']}€")
        print(f"> Valor Final: {forn['valorFinal']}€")

def menu():
    
    print("\n| Construção Banana Inc. |")
    print("[1] - Inserir dados de fornecedor")
    print("[2] - Listar fornecedores")
    print("[3] - Procurar fornecedor por numero")
    print("[0] - Sair\n")
    try:
        resp = int(input("->"))
    except:
        print("\n--!! Valor inserido invalido !!--\n")
        return
    if resp == 1:
        insertForn()
    elif resp == 2:
        listaForns()
    elif resp == 3:
        print("\n--- Procurar Cliente ---")
        encontrado = False
        try:
            num_busca = int(input("Insira o número do fornecedor: "))
            for forn in fornecedoresList:
                if forn["numFor"] == num_busca:
                    print(f"\n| Fornecedor nº{forn['numFor']}")
                    print(f"> Nome: {forn['nome']}")
                    print(f"> Endereco: {forn['endereco']}")
                    print(f"> Telefone: {forn['telefone']}")
                    print(f"> NIF: {forn['nif']}")
                    print(f"> Valor Fornecido: {forn['valorFornecido']:.2f}€")
                    print(f"> Valor Final: {forn['valorFinal']:.2f}€")
                    encontrado = True
                    break
            if not encontrado:
                print("!! Fornecedor nao encontrado !!")
        except ValueError:
            print("!! Valor inserido invalido !!")
    elif resp==0:
        print("\n| Ate a proxima! |\n")
        return True
    else:
        print("\n-- !! Opcao invalida !! --\n")
        menu()
        
while True:
    if menu():
        break