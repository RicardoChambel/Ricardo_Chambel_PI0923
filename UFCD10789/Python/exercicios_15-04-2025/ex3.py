#Ler a nota de 10 alunos, calcular a media e mostrar essa média.

cont = 0
media = 0
notas = []

while cont!=10:
    try:
        inserido = int(input("Insira um numero: "))
        notas.append(inserido)
        cont += 1
    except ValueError:
        print("Valor incorreto!")
        continue
cont = 0
for i in notas:
    media += i
    cont += 1

media = media / cont
print("Media: ", media)