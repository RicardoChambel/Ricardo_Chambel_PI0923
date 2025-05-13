import requests

user_ids = []

id = 7194
f = open("id_1.txt", "a")
for id in range(7194, 8000):
  print("---- A procurar no ID: ", id)
  resposta = requests.get(f'https://trainingserver.atec.pt/TrainingServer/Mulberry/JSON/Controls/Calendar/getCalendarDataSource.ashx?command=_SelectAllSchedulesDataSetGivenByUserId&oId={id}&idField=DataValueField&titleField=DataTextField&startDateField=DataStartField&endDateField=DataEndField&backgroundColorField=&textColorField=textcolor&eventColorField=color&description=description&picField=pic&urlField=url&start=1747004400&end=1747609200&_=1747127413405')

  if "Sessão como Formador" in resposta.text and ("Rogelio" in resposta.text or "Rogélio" in resposta.text):
    user_ids.append(id)
    f.write(str(id)+'\n')
  else:
    print("[x] O Formador Rogélio não foi encontrado como formador no horario do ID: ", id)

f.close
print("-- ID's Encontrados --")
for i in user_ids:
  print(i,'\n')

