import data from "../database/saude_novos.json";

const findAll = () => {
    return data
}

const findMunicipio = (MUNICIPIO: any) =>{
    return data.filter(item => item.MUNICIPIO === MUNICIPIO)
}

export {
    findAll,
    findMunicipio
}
