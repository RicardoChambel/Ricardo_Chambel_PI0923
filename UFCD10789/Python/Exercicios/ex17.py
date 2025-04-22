# Elabore um programa que determine os múltiplos de 5 mas não múltiplos de 3 …. 
# De 1 a 1000 deve ser a sequência.

mult_cinco = []

for i in range(1, 1000+1):
    print(i)
    if i % 5 == 0:
        if  i % 3 != 0:
            mult_cinco.append(i)

print("Multiplos de 5 (sem multiplos de 3): ", mult_cinco)
