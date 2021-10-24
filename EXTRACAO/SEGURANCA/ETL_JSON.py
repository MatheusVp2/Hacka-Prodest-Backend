import json
from pprint import pprint

with open('./seguranca.json', 'r', encoding="UTF-8") as fs:
    json_data = json.load(fs)

def getJsonSeguranca(dado):
    return {
        "LONG"       : dado['COORDX'],
        "LAT"        : dado['COORDY'],
        "AGENCIA"    : dado['AGENCIA'],
        "NOME"       : dado['NOME'],
        "NOME_MUNIC" : dado['NOME_MUNIC'],
        "LOGRADOURO" : dado['LOGRADOURO']
    }

novosDados = []

for dado in json_data:
    novosDados.append(getJsonSeguranca(dado))

with open("./seguranca_novos.json", "w", encoding="UTF-8") as fs:
    json.dump(novosDados, fs, ensure_ascii=False, indent=4)