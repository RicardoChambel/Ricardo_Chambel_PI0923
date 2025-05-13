# RESOLUCAO MINHA:
# TRANSFORMAR A RESPOSTA DO URL PARA UM .TXT COM ENCODING CORRETO
# DE SEGUIDA
# TRANSFORMAR O TEXTO .TXT PARA UM .JSON
# VERIFICAR DESCRIÇÕES TODAS DO FICHEIRO .JSON
# ENCONTRAR O FICHEIRO CUJAS DESCRIÇÕES TODAS TENHAM ROGÉLIO 
# TRANSLATOR: https://jsonlint.com/

import requests

ficheiros_ids = ["id_1.txt","id_2.txt","id_3.txt","id_4.txt","id_5.txt"]
user_ids = []

# METER OS IDS TODOS NO FICHEIRO DE IDS ENCONTRADOS
with open("ids_encontrados.txt", "r") as f:
    for linha in f:
        linha = linha.strip()
        if linha.isdigit():
            user_ids.append(int(linha))

print(user_ids)

#id = 7194
#f = open("id_1.txt", "a")
#for id in range(7194, 8000):
#  print("---- A procurar no ID: ", id)
#  resposta = requests.get(f'https://trainingserver.atec.pt/TrainingServer/Mulberry/JSON/Controls/Calendar/getCalendarDataSource.ashx?command=_SelectAllSchedulesDataSetGivenByUserId&oId={id}&idField=DataValueField&titleField=DataTextField&startDateField=DataStartField&endDateField=DataEndField&backgroundColorField=&textColorField=textcolor&eventColorField=color&description=description&picField=pic&urlField=url&start=1747004400&end=1747609200&_=1747127413405')

#  if "Sessão como Formador" in resposta.text and ("Rogelio" in resposta.text or "Rogélio" in resposta.text):
#    user_ids.append(id)
#    f.write(str(id)+'\n')
#  else:
#    print("[x] O Formador Rogélio não foi encontrado como formador no horario do ID: ", id)

#f.close
#print("-- ID's Encontrados --")
#for i in user_ids:
#  print(i,'\n')


# TRANSFORMAR RESPOSTA PARA .TXT COM ENCODING CORRETO
#id = 9838
#f = open("verify.txt", "wb")
#print("---- A importar o request do ID ", id)
#resposta = requests.get(f'https://trainingserver.atec.pt/TrainingServer/Mulberry/JSON/Controls/Calendar/getCalendarDataSource.ashx?command=_SelectAllSchedulesDataSetGivenByUserId&oId={id}&idField=DataValueField&titleField=DataTextField&startDateField=DataStartField&endDateField=DataEndField&backgroundColorField=&textColorField=textcolor&eventColorField=color&description=description&picField=pic&urlField=url&start=1747004400&end=1747609200&_=1747127413405')
#f.write(resposta.content)
#f.close

