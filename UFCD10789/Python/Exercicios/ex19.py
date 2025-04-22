# Escreva um programa que mostre os primeiros
# 1, 1, 2, 3, 5, 8, 13, 21

# Como se constrói
# 1+1=2
# 1+2=3
# 2+3=5

fim = int(input("Insira a quantidade de numeros da sequencia de Fibonacci: "))

if fim <= 0:
    print("Tem de inserir um valor maior que 0!")
else:
    anterior = 1
    now = 1

    if fim >= 1:
        print(anterior)
    if fim >= 2:
        print(now)

    for i in range(3, fim+1):
        aft = anterior + now
        anterior = now
        now = aft
        print(aft)
