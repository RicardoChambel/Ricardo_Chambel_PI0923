# Crie um algoritmo que leia um número inteiro, e diga se ele é um número primo ou não
num = int(input("Insira um numero:"))
if (num%2==0 and num!=2) or (num%3==0 and num!=3):
    print("Numero não é primo")
else:
    print("Numero é primo")