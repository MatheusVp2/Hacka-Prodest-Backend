import data from "../database/seguranca_novos.json";

const findAll = () => {
    return data
}

const findByAgencia = (agencia: string) => {
    return data.filter( item =>  item.AGENCIA === agencia )
}

export {
    findAll,
    findByAgencia
}
