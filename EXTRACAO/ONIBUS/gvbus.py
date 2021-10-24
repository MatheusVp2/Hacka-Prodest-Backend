import requests
from pprint import pprint

url = "https://sistemas.es.gov.br/webservices/ceturb/onibus/api/BuscaHorarios/560"
url1= "https://sistemas.es.gov.br/webservices/ceturb/onibus/api/BuscaItinerarios/815"
tiposLinha = "https://sistemas.es.gov.br/webservices/ceturb/onibus/api/ConsultaLinha/?Tipo_Linha=T"

res = requests.get(url).json()
pprint(res)
