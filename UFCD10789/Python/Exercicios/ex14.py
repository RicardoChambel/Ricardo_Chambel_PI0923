# Altere o programa anterior para que mostre todas as tabuadas de 1 a 100. 
# (ciclos for).

for i in range(1, 100+1):
    print(f"\nTabuada de {i}")
    for y in range(1, 10+1):
        print(f"{i} x {y} = ", i*y)