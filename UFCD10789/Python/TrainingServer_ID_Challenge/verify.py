import requests

ficheiros_ids = ["id_1.txt","id_2.txt","id_3.txt","id_4.txt","id_5.txt"]

with open("ids_encontrados.txt", "w") as f:
    for ficheiro in ficheiros_ids:
        with open(ficheiro, "r") as f:
            for linha in f:
                linha = linha.strip()
                if linha.isdigit():
                    f.write(str(linha) + "\n")

#id = 9838
#f = open("verify.txt", "wb")
#print("---- A importar o request do ID ", id)
#resposta = requests.get(f'https://trainingserver.atec.pt/TrainingServer/Mulberry/JSON/Controls/Calendar/getCalendarDataSource.ashx?command=_SelectAllSchedulesDataSetGivenByUserId&oId={id}&idField=DataValueField&titleField=DataTextField&startDateField=DataStartField&endDateField=DataEndField&backgroundColorField=&textColorField=textcolor&eventColorField=color&description=description&picField=pic&urlField=url&start=1747004400&end=1747609200&_=1747127413405')
#f.write(resposta.content)
#f.close

