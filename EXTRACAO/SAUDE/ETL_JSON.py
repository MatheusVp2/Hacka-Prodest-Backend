import json

with open('./saude.json', 'r', encoding="UTF-8") as fs:
    json_data = json.load(fs)

def getJsonSaude(dado):
    return {
        "LONG"       : dado['COORDX'],
        "LAT"        : dado['COORDY'],
        "NOME"       : dado['NOME'],
        "MUNICIPIO"  : dado['MUNICIPIO'],
        "CEP"        : dado['CEP'],
        "LOGRADOURO" : dado["LOGRADOURO"],
        "TELEFONE"   : dado["TELEFONE"],
        "EMAIL"      : dado["EMAIL"].strip("\"\"")
    }

novosDados = []

for dado in json_data:
    novosDados.append( getJsonSaude(dado) )

with open("./saude_novos.json", "w", encoding="UTF-8") as fs:
    json.dump(novosDados, fs, ensure_ascii=False, indent=4)