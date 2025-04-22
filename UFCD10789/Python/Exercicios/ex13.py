# Elabore um programa que leia um número e mostre a tabuada. 
# (multiplicar de 1 a 10)

num = int(input("Insira um numero:\n->"))

for i in range(1, 10+1):
    print(f"{num} x {i} = ", num*i)