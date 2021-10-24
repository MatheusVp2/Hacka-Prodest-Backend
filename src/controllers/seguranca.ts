import { Request, Response, Router } from 'express';
import { findAll,findByAgencia,findMunicipio } from "../repository/segurancaRep";


export default {

    get : async (req: Request, res: Response) => {
        const data = findAll()
        return res.status(200).json({ quantidade: data.length ,dados: data})
    },

    getFiltro : async (req: Request, res: Response) => {
        const {tipo,municipio} = req.query
        let data
        if (municipio && tipo){
            data = findByAgencia(tipo)
            data = data.filter(item => item.MUNICIPIO === municipio) 
        }
        else if (municipio){
            data = findMunicipio(municipio)
        }
        else if (tipo){
            data = findByAgencia(tipo)
        }
        else{
            data = findAll()
        }

        return res.status(200).json({ quantidade: data.length ,dados: data})
    },

    post : async (req: Request, res: Response) => {

        return res.status(200).json({ ok: true})
    }

}

