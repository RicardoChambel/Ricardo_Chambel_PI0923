# Elabore um programa que escreva no ecrã todas as linhas de código ASCII(0 a 255) e o 
# código correspondente. 
# Dispor de 20 em 20 com a condição de continuação ou saída do programa.

disp = 0

while disp < 256:
    for j in range(disp, disp + 20):
        if j > 255:
            break

        valor = chr(j)
        if valor.isprintable():
            print("Código", j, "=", valor)
        else:
            print("Código", j, "= (não é possivel mostrar)")
            
    disp += 20

    resposta = input("\nPrima Enter para continuar ou escreva 'sair' para terminar: ")
    if resposta.lower() == "sair":
        break




