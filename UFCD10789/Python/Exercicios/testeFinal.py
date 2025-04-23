# Elabore um programa que leia um valor de entrada e mostre para cada valor até ao 1
# (se é número Primo, Quantos divisores e números perfeitos) o Programa deve validar entradas entre 
# 1 e 30.000, e parar de 10 em 10 valores com instrução para parar ou continuar. 
# No mesmo programa use um menu e Elabore uma calculadora simples (+,-,*,/) com a função extra tabuada.
# Validar entradas de 1 a 1000 (nota a tabuada deve apresentar todas as multiplicações de 1 ate ao máximo 
# introduzido) deve parar de 20 em 20 valores.

ligado = True

while ligado:
    print("\n------ MENU -------")
    print("[1] Analisar numeros de x ate 1")
    print("[2] Calculadora")
    print("[3] Sair")

    opcao = input("Escolha ->")

    if opcao == '1':
        while True:
            try:
                valor = int(input("Insira um valor (x) de 1 a 30000 ->"))
                if 1 <= valor <= 30000:
                    break
                else:
                    print("!! Valor fora do intervalo!!")
            except ValueError:
                print("!! Entrada invalida!!")

        contador = 0
        for i in range(valor, 0, -1):
            print(f"\n--- Numero {i} ---")

            # Verificar se é primo
            primo = True
            if i <= 1:
                primo = False
            elif i == 2:
                primo = True
            elif i % 2 == 0:
                primo = False
            else:
                for j in range(3, int(i**0.5) + 1, 2):
                    if i % j == 0:
                        primo = False
                        break

            print("-- É numero primo" if primo else "-- Nao é numero primo")

            # Divisores
            divs = []
            for j in range(1, i+1):
                if i % j == 0:
                    divs.append(j)
            print("-- Divisores:", divs)

            # Número Perfeito
            soma_divs = sum(divs) - i
            perfeito = soma_divs == i
            print("-- Numero Perfeito:", "Sim" if perfeito else "Não")

            contador += 1
            if contador % 10 == 0:
                continuar = input("\nDeseja continuar? (s/n): ").lower()
                if continuar != 's':
                    break

    elif opcao == '2':
        while True:
            print("\n------- CALCULADORA -------")
            print("[1] Adicao (+)")
            print("[2] Subtracao (-)")
            print("[3] Multiplicacao (*)")
            print("[4] Divisao (/)")
            print("[5] Tabuada")
            print("[6] Voltar ao menu principal")

            escolha = input("Escolha uma opcao ->")

            if escolha in ['1', '2', '3', '4']:
                try:
                    a = float(input("Primeiro numero ->"))
                    b = float(input("Segundo numero ->"))
                    if escolha == '1':
                        print(f"-- Resultado: {a + b}")
                    elif escolha == '2':
                        print(f"-- Resultado: {a - b}")
                    elif escolha == '3':
                        print(f"-- Resultado: {a * b}")
                    elif escolha == '4':
                        if b == 0:
                            print("!! Erro: Divisao por zero!!")
                        else:
                            print(f"-- Resultado: {a / b}")
                except ValueError:
                    print("!! Entrada invalida!!")

            elif escolha == '5':
                while True:
                    try:
                        maximo = int(input("Gerar tabuada ate que numero? (1 a 1000) -> "))
                        if 1 <= maximo <= 1000:
                            break
                        else:
                            print("!! Insira um valor entre 1 e 1000!!")
                    except ValueError:
                        print("!! Entrada invalida!!")

                contador_tabuada = 0
                for i in range(1, maximo + 1):
                    print(f"\nTabuada do {i}")
                    for j in range(1, 11):
                        print(f"-- {i} x {j} = {i*j}")

                    contador_tabuada += 1
                    if contador_tabuada % 20 == 0:
                        continuar = input("\nDeseja continuar? (s/n) -> ").lower()
                        if continuar != 's':
                            break

            elif escolha == '6':
                break
            else:
                print("!! Opcao invalida!!")

    elif opcao == '3':
        print("-- Ate a proxima!")
        ligado = False

    else:
        print("!! Opcao invalida!!")