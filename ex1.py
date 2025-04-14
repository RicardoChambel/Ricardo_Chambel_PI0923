# Entre 3 numeros, saber maior, meio e menor

num1 = int(input("Num1: "))
num2 = int(input("Num2: "))
num3 = int(input("Num3: "))

print("\n Versão Original \n")
# Versão Original
if num1>num2 and num2>num3:
        print("[if 1]") # Debug
        print(f"Maior: {num1}")
        print(f"Meio: {num2}")
        print(f"Menor: {num3}")
elif num1>num2 and num3>num2 and num1>num3:
        print("[if 2]") # Debug
        print(f"Maior: {num1}")
        print(f"Meio: {num3}")
        print(f"Menor: {num2}")
elif num2>num1 and num1>num3:
        print("[if 3]") # Debug
        print(f"Maior: {num2}")
        print(f"Meio: {num1}")
        print(f"Menor: {num3}")
elif num2>num1 and num2>num3:
        print("[if 4]") # Debug
        print(f"Maior: {num2}")
        print(f"Meio: {num3}")
        print(f"Menor: {num1}")
elif num3>num1 and num1>num2:
        print("[if 5]") # Debug
        print(f"Maior: {num3}")
        print(f"Meio: {num1}")
        print(f"Menor: {num2}")
else:
        print("[else]") # Debug
        print(f"Maior: {num3}")
        print(f"Meio: {num2}")
        print(f"Menor: {num1}")

print("\n Versão mais Legivel \n")
# Versão mais Legivel
if num1>num2 and num1>num3:
    if num2>num3:
        print("[if 1 -> if]") # Debug
        print(f"Maior: {num1}")
        print(f"Meio: {num2}")
        print(f"Menor: {num3}")
    else:
        print("[if 1 -> else]") # Debug
        print(f"Maior: {num1}")
        print(f"Meio: {num3}")
        print(f"Menor: {num2}")
elif num2>num1 and num2>num3:
    if num1>num3:
        print("[if 2 -> if]") # Debug
        print(f"Maior: {num2}")
        print(f"Meio: {num1}")
        print(f"Menor: {num3}")
    else:
        print("[if 2 -> else]") # Debug
        print(f"Maior: {num2}")
        print(f"Meio: {num3}")
        print(f"Menor: {num1}")
else:
    if num1>num2:
        print("[else -> if]") # Debug
        print(f"Maior: {num3}")
        print(f"Meio: {num1}")
        print(f"Menor: {num2}")
    else:
        print("[else -> else]") # Debug
        print(f"Maior: {num3}")
        print(f"Meio: {num2}")
        print(f"Menor: {num1}")