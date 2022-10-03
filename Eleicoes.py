import requests
import json
import pandas as pd
import time

while True:
    data = requests.get(
        'https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/br/br-c0001-e000544-r.json')
    json_data = json.loads(data.content)

    candidato = []
    votos = []
    porcentagem = []
    porcentagemtotal = json_data['pst']

    for informacoes in json_data['cand']:
        
        candidato.append(informacoes['nm'])
        votos.append(informacoes['vap'])
        porcentagem.append(informacoes['pvap'])

    df_eleicao = pd.DataFrame(list(zip(candidato, votos, porcentagem)), columns=[
                            'Candidato','N Votos','Porcentagem'])
    print("----------------------------------------------")
    print("Votos apurados =",porcentagemtotal,"%")
    print(df_eleicao)
    time.sleep(15)
