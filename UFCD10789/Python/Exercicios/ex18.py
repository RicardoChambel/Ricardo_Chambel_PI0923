# Elabore um programa que leia uma entrada e diga quantos números perfeitos existem. 
# Exemplo de numero perfeito em que somando todos os divisores ele da o numero inicial.
# 6=3+2+1

num = int(input("Insira um numero para verificar:\n->"))

sum = 0
for i in range(1, num):
    if num % i == 0:
        sum+=i

if sum==num:
    print(f"O numero {num} é perfeito!")
else:
    print(f"O numero {num} não é perfeito :(")

