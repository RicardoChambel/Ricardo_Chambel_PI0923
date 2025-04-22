#Ler 10 números, e determinar se o número par e número impar.

cont = 0
par = []
impar = []

while cont!=10:
    try:
        num = int(input("Insira um numero: "))
        if num%2==0:
            par.append(num)
        else:
            impar.append(num)
        cont += 1
    except ValueError:
        print("Valor incorreto!")
        continue

print(f"Numeros pares inseridos: {par}")
print(f"Numeros ímpares inseridos: {impar}")
