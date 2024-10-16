import json
import numpy as np
from datetime import datetime, timedelta

def menor_faturamento(data):
    data_list=data['faturamento_diario']
    faturamentos = [dia['faturamento'] for dia in data_list]
    return min(faturamentos)

def maior_faturamento(data):
    data_list=data['faturamento_diario']
    faturamentos = [dia['faturamento'] for dia in data_list]
    return max(faturamentos)

def media_faturamento(data):
    data_list=data['faturamento_diario']
    faturamentos = [dia['faturamento'] for dia in data_list]
    media_mensal=np.mean(faturamentos)

    valores_maiores=[dia['dia'] for dia in data_list if dia['faturamento'] > media_mensal]
 
    return len(valores_maiores),

with open('faturamento.json','r') as f:
    faturamentojson=json.load(f)

print("Menor faturamento mensal: {}\nMaior faturamento mensal: {} \nDias com valores maiores que a média: {}\n".format(
menor_faturamento(faturamentojson),
maior_faturamento(faturamentojson),
media_faturamento(faturamentojson)))