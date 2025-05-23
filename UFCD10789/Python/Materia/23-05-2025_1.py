cliname=[]
opc=0

while True:
    print("1 - Inserir nome do cliente")
    print("2 - Listar clientes")
    print("3 - Sair da app")
    opc = input(">")
    match opc:
        case "1":
            cliname.append(input("Nome a inserir: "))
        case "2":
            for x in cliname:
                print("- ", x)
        case "3":
            print("Adios muxaxus")
            break
        case _:
            print("- Opção inválida -")