from os import getlogin
from geopy.geocoders import Nominatim
from pycep_correios import get_address_from_cep, WebService
import re

def buscaEnderecoCompleto(cep):
    try:
        busca = get_address_from_cep(cep, webservice=WebService.APICEP)
        endereco = "{} {} {}".format(busca["logradouro"], busca["cidade"],   busca["uf"] )
        return endereco
    except:
        pass
    try:
        busca = get_address_from_cep(cep, webservice=WebService.VIACEP)
        endereco = "{} {} {}".format(busca["logradouro"], busca["cidade"],   busca["uf"] )
        return endereco
    except:
        pass

    try:
        busca = get_address_from_cep(cep, webservice=WebService.CORREIOS)
        endereco = "{} {} {}".format(busca["logradouro"], busca["cidade"],   busca["uf"] )
        return endereco
    except:
        pass

    return None

def buscaLatitudeLongitude(cep=None, endereco=None):
    if cep:
        endereco = buscaEnderecoCompleto(cep)

    if not endereco:
        return [None, None]

    try:
        locator = Nominatim(user_agent="geoCoders")
        location = locator.geocode(endereco)
        if location:
            return [ str(location.latitude), str(location.longitude) ]
    except Exception as e:
        return None

    return [None, None]

def getCepTexto(texto):
    regexCEP = "([0-9]{8})"
    ceps = re.findall(regexCEP, texto)
    if len(ceps) == 0:
        return None
    return ceps[0]



