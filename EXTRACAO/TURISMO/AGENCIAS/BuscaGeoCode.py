from os import getlogin
from geopy.geocoders import Nominatim
from pycep_correios import get_address_from_cep, WebService
import re

import logging, coloredlogs


def settingsColor():
    format = '%(asctime)s | %(name)s | %(levelname)s => %(message)s'
    coloredlogs.install(level=logging.INFO, fmt=format)

def getLoggerAplication(className="root"):
    return logging.getLogger(name=className)

settingsColor()
logApi = getLoggerAplication("API CEP")
logApiCord = getLoggerAplication("API CORD")

def buscaEnderecoCompleto(cep):
    try:
        logApi.info("Buscando Endereco 1")
        busca = get_address_from_cep(cep, webservice=WebService.APICEP)
        endereco = "{} {} {}".format(busca["logradouro"], busca["cidade"],   busca["uf"] )
        return endereco
    except:
        logApi.warning("Erro: Primeira Chamada")
        pass
    try:
        logApi.info("Buscando Endereco 2")
        busca = get_address_from_cep(cep, webservice=WebService.VIACEP)
        endereco = "{} {} {}".format(busca["logradouro"], busca["cidade"],   busca["uf"] )
        return endereco
    except:
        logApi.warning("Erro: Segunda Chamada")
        pass

    try:
        logApi.info("Buscando Endereco 3")
        busca = get_address_from_cep(cep, webservice=WebService.CORREIOS)
        endereco = "{} {} {}".format(busca["logradouro"], busca["cidade"],   busca["uf"] )
        return endereco
    except:
        logApi.warning("Erro: Terceira Chamada")
        pass

    return None

def buscaLatitudeLongitude(cep=None, endereco=None):
    if cep:
        endereco = buscaEnderecoCompleto(cep)

    if not endereco:
        return [None, None]

    try:
        logApiCord.info("Buscando Coordenada")
        locator = Nominatim(user_agent="geoCoders")
        location = locator.geocode(endereco)
        if location:
            return [ str(location.latitude), str(location.longitude) ]
    except Exception as e:
        logApiCord.warning("Erro: Busca Latitude Longitude")
        print(e)
        return None

    return [None, None]

def getCepTexto(texto):
    regexCEP = "([0-9]{8})"
    ceps = re.findall(regexCEP, texto)
    if len(ceps) == 0:
        return None
    return ceps[0]


texto = "Coronel Pedro Maia de Carvalho LOJA  1 Vila Velha Praia das Gaivotas CEP: 29102570 ES"
cep = getCepTexto(texto)

logApi.info(f"CEP ENCONTRADO: {cep}")
