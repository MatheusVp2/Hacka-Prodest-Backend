import json
from BuscaGeoCode import buscaLatitudeLongitude, getCepTexto

with open('EXTRACAO\\ONIBUS\\pontosOnibus.json', 'r', encoding="UTF-8") as fs:
    json_data = json.load(fs)

def getJsonAgencia(texto):
    lat  = None
    long = None

    cep = getCepTexto(texto)

    if cep:
        lat, long = buscaLatitudeLongitude(cep=cep)
    
    if not lat:
        lat, long = buscaLatitudeLongitude(endereco=texto)

    if not lat:
        lat, long = buscaLatitudeLongitude(endereco=texto)

    return {
        "LONG"       : long,
        "LAT"        : lat,
    }
cont=0
novosDados = []
for dado in json_data["pontos"]:
    try:
        data = getJsonAgencia(dado)
        novosDados.append(data)
    except:
        pass
    cont+=1

with open("EXTRACAO\\ONIBUS\\novos_pontosOnibus.json", "w", encoding="UTF-8") as fs:
    json.dump(novosDados, fs, ensure_ascii=False, indent=4)