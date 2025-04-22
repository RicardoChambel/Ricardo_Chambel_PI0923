#Crie um algoritmo que mostre os 10 primeiros números primos.

primo = 0
cont = 0

while cont<=10:
    if (primo%2==0 and primo!=2) or (primo%3==0 and primo!=3):
        primo+=1
    else:
        print(primo)
        primo+=1
        cont+=1
