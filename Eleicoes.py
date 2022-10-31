import requests
import json
import pandas as pd
import time
import os

# WHILE UTILIZADO PARA REPETIR O PROCESSO

while True:

    # SISTEMA DE REQUEST DE INFORMAÇÕES DO SITE

    data = requests.get(
        'https://resultados.tse.jus.br/oficial/ele2022/545/dados-simplificados/br/br-c0001-e000545-r.json')
    json_data = json.loads(data.content)

    # CRIANDO LISTAS PARA GUARDAR INFORMAÇÕES

    candidato = []
    votos = []
    porcentagem = []
    porcentagemtotal = json_data['pst']

    # ADICIONANDO INFORMAÇÕES AS LISTAS

    for informacoes in json_data['cand']:
        candidato.append(informacoes['nm'])
        votos.append(informacoes['vap'])
        porcentagem.append(informacoes['pvap'])

    # CRIAÇÃO DE TABELA

    df_eleicao = pd.DataFrame(list(zip(candidato, votos, porcentagem)), columns=[
        'Candidato', 'N Votos', 'Porcentagem'])

    # PRINT DE TODO O RESULTADO

    os.system('cls')                                    # LIMPA O CONSOLE ANTES DE PRINTAR UM NOVO RESULTADO
    print("Votos apurados =", porcentagemtotal, "%")    # PRINT DA PORCENTAGEM TOTAL DE VOTOS
    print("")                                           # PULA LINHA
    print(df_eleicao)                                   # PRINT DA TABELA
    time.sleep(10)                                      # A CADA 10 SEGUNDO RETORNA PARA O WHILE TRUE
