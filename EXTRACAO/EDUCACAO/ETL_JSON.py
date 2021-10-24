import json
from pprint import pprint

with open('./educacao.json', 'r', encoding="UTF-8") as fs:
    json_data = json.load(fs)

def getJsonEducacao(dado):
    return {
        "LONG"       : dado['COORDX'],
        "LAT"        : dado['COORDY'],
        "LOGRADOURO" : dado["LOGRADOURO"],
        "TELEFONE"   : dado["TELEFONE"],
        "CLASSECNAE" : dado["CLASSECNAE"],
        "MUNICIPIO"  : dado["MUNICIPIO"],
        "BAIRRO"     : dado["BAIRRO"],
        "NOMEABREV"  : dado["NOMEABREV"],
        "SIGLAEXTEN" : dado["SIGLAEXTEN"],
        "NOME"       : dado["NOME"],
        "CEP"        : dado["CEP"]
    }

novosDados = []
carai = [  ]

for dado in json_data:
    if dado['OPERACION'] == 'Sim':
        novosDados.append(getJsonEducacao(dado))

with open("./educacao_novos.json", "w", encoding="UTF-8") as fs:
    json.dump(novosDados, fs, ensure_ascii=False, indent=4)