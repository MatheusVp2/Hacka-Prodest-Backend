import requests
from pprint import pprint
import json

# url = "https://sistemas.es.gov.br/webservices/ceturb/onibus/api/BuscaHorarios/560"
rotas= "https://sistemas.es.gov.br/webservices/ceturb/onibus/api/BuscaItinerarios/"
linhas = "https://sistemas.es.gov.br/webservices/ceturb/onibus/api/ConsultaLinha??Tipo_Linha=T"

resLinhas = requests.get(linhas).json()


lista = []
for linha in range(len(resLinhas)):
    resRotas = requests.get(rotas+resLinhas[linha]['Linha']).json()
    for rota in resRotas:
        if type(rota) != str:
            lista.append(rota['Desc_Via']+"Espirito Santo")            
        else:
            pass
l = []
for i in lista:
    if i not in l:
        l.append(i)
l.sort()

dict_pontos = {"pontos":l}

with open("EXTRACAO\\ONIBUS\\pontosOnibus.json", "w", encoding="UTF-8") as fs:
    json.dump(dict_pontos, fs, ensure_ascii=False, indent=4)
