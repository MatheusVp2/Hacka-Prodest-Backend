import agencia from "../database/agencias_novos.json";
import hotel from "../database/hospedagem_novos.json";
import locadoraCarro from "../database/locadoras_novos.json";
import restaurante from "../database/restaurantes_novos.json";

const findAll = (tipo:any) => {
    let data
    if (tipo == "agencia"){
        data = agencia
    }
    else if (tipo == "hotel"){
        data = hotel
    }
    else if (tipo == "locadoraCarro"){
        data = locadoraCarro
    }
    else if (tipo == "restaurante"){
        data = restaurante
    }
    return data
}

const findMunicipio = (MUNICIPIO: any,tipo:any) =>{
    let data
    if (tipo == "agencia"){
        data = agencia
    }
    else if (tipo == "hotel"){
        data = hotel
    }
    else if (tipo == "locadoraCarro"){
        data = locadoraCarro
    }
    else if (tipo == "restaurante"){
        data = restaurante
    }
    return data.filter(item => item.MUNICIPIO === MUNICIPIO)
}

export {
    findAll,
    findMunicipio
}