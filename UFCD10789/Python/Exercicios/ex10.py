# Elabore um programa que 
# lê um número e escreve quantos divisores ele possui.

num = int(input("Insira um numero\n->"))

div = 0
divs = []

for i in range(1, num+1):
    if num%i == 0:
        div += 1
        divs.append(i)

print(f"{num} tem {div} divisores")
print("Divisores -> ",divs)
