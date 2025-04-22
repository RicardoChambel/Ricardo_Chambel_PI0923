# Elabore um programa que constitua a média de 30 números pares que sejam introduzidos. 
# Validando a entrada de números inteiros entre 1 e 50

nums = []
cont = 0

while(cont!=30):
    try:
        ins = int(input(f"[{cont+1}] Insira um numero de 1 a 50: "))
    except ValueError:
        ins=0
    if ins<1 or ins>50:
        print("Valor invalido")
    else:
        try:
            nums.append(ins)
            cont+=1
        except:
            continue

media = 0
for i in nums:
    media += i
print("\nTotal: ", media)

media = media / 30
print(media)
print("Media: ", media)
            

