import data from "../database/seguranca_novos.json";

const findAll = () => {
    return data
}

const findByAgencia = (agencia: any) => {
    return data.filter( item =>  item.AGENCIA === agencia )
}

const findMunicipio = (MUNICIPIO: any) =>{
    return data.filter(item => item.MUNICIPIO === MUNICIPIO)
}

export {
    findAll,
    findByAgencia,
    findMunicipio
}
