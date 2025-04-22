#Elabore um programa que leia quantos números quer que se efetue a soma, 
# subtrações, divisões, multiplicações e no fim por meio de um acumulador 
# diga quantas operações foram efetuadas. 
# Exemplo introduzindo o número 60 o programa deve
# apresentar 60 a somar, dividir multiplicar e subtrair por todos os números menores que ele.
print("\nQuantos valores numeros quer efetuem soma, subtracoes, divisoes e multiplicacoes?")
num = int(input("->"))
for i in range(0, num + 1):
    print(f"{num} + {i} = ", num+i)
    print(f"{num} - {i} = ", num-i)
    print(f"{num} * {i} = ", num*i)
    if i!=0:
        print(f"{num} / {i} = ", num/i)
    else:
        print(f"{num} / {i} = 0")
    print("\n")