# Criar menu com 3 opções:
# 1- Introduzir nomes
# 2- Listar nomes
# 3- Parar programa 

nomes = []

ligado = True

while ligado:
    print("Menu")
    print("[1] - Introduzir nomes")
    print("[2] - Listar nomes")
    print("[3] - Parar programa")
    try:
        escolha = int(input("Escolha: "))
    except ValueError:
        print("Valor incorreto")
        continue

    match escolha:
        case 1:
            print("- Inserir nomes -")
            nomes.append(input("Novo nome: "))
            for i in nomes:
                sair = input("Deseja parar? (S ou N)\n->")
                if sair == "S" or sair == "s":
                    break
                nomes.append(input("Novo nome: "))
        case 2:
            print("- Nomes -")
            for i in nomes:
                print(i)
            print("\n")
        case 3:
            ligado = False
            continue
        case default:
            print("Escolha inválida")