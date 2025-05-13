# RESOLUCAO MINHA:
# TRANSFORMAR A RESPOSTA DO URL PARA UM .TXT COM ENCODING CORRETO
# DE SEGUIDA
# TRANSFORMAR O TEXTO .TXT PARA UM .JSON
# VERIFICAR DESCRIÇÕES TODAS DO FICHEIRO .JSON
# ENCONTRAR O FICHEIRO CUJAS DESCRIÇÕES TODAS TENHAM ROGÉLIO 

import requests
import json

ficheiros_ids = ["id_1.txt", "id_2.txt", "id_3.txt", "id_4.txt", "id_5.txt"]
user_ids = []

# 1. LER IDS DOS FICHEIROS
for ficheiro in ficheiros_ids:
    with open(ficheiro, "r") as f:
        for linha in f:
            linha = linha.strip()
            if linha.isdigit():
                user_ids.append(int(linha))

# GUARDAR OS IDS NUM FICHEIRO
with open("ids_encontrados.txt", "w") as f_out:
    for user_id in user_ids:
        f_out.write(f"{user_id}\n")

print(f"[DEBUG] IDs encontrados: {user_ids}")

# VERIFICAR CADA ID
id_confirmado = []

for id in user_ids:
    print(f"--- A verificar o ID {id} ---")
    
    url = f'https://trainingserver.atec.pt/TrainingServer/Mulberry/JSON/Controls/Calendar/getCalendarDataSource.ashx?command=_SelectAllSchedulesDataSetGivenByUserId&oId={id}&idField=DataValueField&titleField=DataTextField&startDateField=DataStartField&endDateField=DataEndField&backgroundColorField=&textColorField=textcolor&eventColorField=color&description=description&picField=pic&urlField=url&start=1747004400&end=1747609200&_=1747127413405'
    
    resposta = requests.get(url)

    try:
        dados = json.loads(resposta.content.decode("utf-8"))
    except Exception as e:
        print(f"Erro a fazer parsing do JSON do ID {id}: {e}")
        continue

    # VERIFICAR TODAS AS DESCRIÇÕES
    todas_descricoes_com_rogelio = True
    for evento in dados:
        descricao = evento.get("description", "")
        if "Rogélio" not in descricao:
            todas_descricoes_com_rogelio = False
            break

    if todas_descricoes_com_rogelio and len(dados) > 0:
        print(f"!! O ID {id} é do Rogélio !!")
        id_confirmado.append(id)
        break
    else:
        print(f"[x] O ID {id} não é do Rogélio")

# GUARDAR IDS CONFIRMADOS
with open("id_rogelio.txt", "w") as f_rogelio:
    for id in id_confirmado:
        f_rogelio.write(f"{id}\n")

print(f"\n✅ ID do Rogélio: {id_confirmado}")
