# Elabore um programa que escreva no ecrã todas as linhas de código ASCII(0 a 255) e o 
# código correspondente. 
# Dispor de 20 em 20 com a condição de continuação ou saída do programa.

while(True):
    print("\n")
    inicio = 0
    fim = 255
    passo = 20

    while inicio < fim:
        for i in range(inicio, min(inicio + passo, fim+1)):
            try:
                print(f"Código {i} = '{chr(i)}'")
            except:
                print(f"Código {i} = Não representável")

        inicio += passo
        escolha = input("\nPrima Enter para continuar ou escreva 'sair' para terminar: ")
        if escolha.lower() == 'sair':
            break