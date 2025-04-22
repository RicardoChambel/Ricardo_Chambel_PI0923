#Elabore um ciclo for para produzir o seguinte output.
#1
#22
#333
#4444
#55555

tamanho = int(input("Insira um numero: "))

for i in range(1, tamanho+1):
    print(f"{i}" * i)