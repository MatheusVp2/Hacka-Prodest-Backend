import json
from BuscaGeoCode import buscaLatitudeLongitude, getCepTexto, settingsColor, getLoggerAplication
import time

settingsColor()

logApp = getLoggerAplication("APLICACAO")

with open('./locadoras.json', 'r', encoding="UTF-8") as fs:
    json_data = json.load(fs)

def getJsonAgencia(dado):
    lat  = None
    long = None

    texto = dado['ENDERECO_COMPLETO_COMERCIAL']
    logApp.info("Buscando CEP")
    cep = getCepTexto(texto)
    print("Buscando CEP: ", cep)
    # logApp.info("Buscando CEP: ", cep)

    if cep:
        logApp.warning("Bucando Latitude pelo CEP")
        lat, long = buscaLatitudeLongitude(cep=cep)
    
    if not lat:
        logApp.warning("Bucando Latitude pelo Endereco")
        lat, long = buscaLatitudeLongitude(endereco=texto)

    if not lat:
        logApp.warning("Bucando Latitude pelo Segundo Endereco")
        texto = dado['ENDERECO_COMPLETO_ESTADO']
        lat, long = buscaLatitudeLongitude(endereco=texto)

    return {
        "LONG"       : long,
        "LAT"        : lat,
        "NUMERO_CNPJ" : dado['NUMERO_CNPJ'],
        "NOME_PESSOA_JURIDICA" : dado['NOME_PESSOA_JURIDICA'],
        "NOME_FANTASIA": dado['NOME_FANTASIA'],
        "ENDERECO_COMPLETO_ESTADO" : dado['ENDERECO_COMPLETO_ESTADO'],
        "ENDERECO_COMPLETO_COMERCIAL" : dado['ENDERECO_COMPLETO_COMERCIAL'],
        "MUNICIPIO" : dado['MUNICIPIO'],
        "UF" : dado['UF'],
        "NOME_RESPONSAVEL" : dado['NOME_RESPONSAVEL'],
        "TELEFONE" : dado['TELEFONE'],
        "EMAIL_ADM" : dado['EMAIL_ADM'],
        "EMAIL_INSTITUTO" : dado['EMAIL_INSTITUTO'],
        "TELEFONE_COMERCIAL" : dado['TELEFONE_COMERCIAL'],
        "EMAIL_COMERCIAL" : dado['EMAIL_COMERCIAL'],
        "WEBSITE" : dado['WEBSITE'],
    }

novosDados = []
conta = 0
for dado in json_data:
    try:
        print(conta)
        data = getJsonAgencia(dado)
        novosDados.append(getJsonAgencia(data))
        conta+=1
    except:
        pass

with open("./locadoras_novos.json", "w", encoding="UTF-8") as fs:
    json.dump(novosDados, fs, ensure_ascii=False, indent=4)