numeros = [1, 2, 4, 8, 10]
# index    0  1  2  3  4

opc = 0
while True:
    print("\n--- Opções ---")
    print("\n[1] - List")
    print("\n[2] - Insert")
    print("\n[3] - Delete")
    print("\n[4] - Search")
    print("\n[4] - Exit")
    opc =int(input("Option: "))
    match opc:
        case 1:
            # Listar conteúdo da lista
            for n in numeros:
                print(n)
            for i in range(len(numeros)):
                print(numeros[i])
        case 2:
            # Inserir na lista
            while True:
                numeros.append(int(input("Insert number: ")))
                resp=input("'Y' to stop: ")
                if resp.lower()=="y":
                    break
        case 3:
            # Delete na lista
            numeros.remove(int(input("Number to delete: ")))
        case 4:
            # Procurar na lista
            search = int(input("Number to search in list: "))
            found = False
            for i in range(len(numeros)):
                if numeros[i]==search:
                    print("Number found in list! | index:", numeros[i])
                    found = True
            if not found:
                print("Number wasn't found in list!")
                    
        case 5:
            break
        case default:
            print("\n-- Opção inválida!\n")
