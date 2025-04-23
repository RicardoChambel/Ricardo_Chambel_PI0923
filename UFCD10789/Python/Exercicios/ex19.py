# Escreva um programa que mostre os primeiros 60 numeros da sequencia de Fibonnacci
# 1, 1, 2, 3, 5, 8, 13, 21

# Como se constrói
# 1+1=2
# 1+2=3
# 2+3=5

fim = 60
anterior = 1
now = 1

print(anterior)
print(now)
for i in range(3, fim+1):
    aft = anterior + now
    anterior = now
    now = aft
    print(aft)
