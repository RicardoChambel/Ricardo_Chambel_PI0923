#Crie um algoritmo que mostre os 30 primeiros números ímpares e pares.

imp=[]
par=[]
num = 0

while num/2!=30:
    if num%2==0:
        par.append(num)
    else:
        imp.append(num)
    num += 1

print(imp)
print(par)
print(num)