import { Request, Response } from 'express';
import { findAll,findMunicipio } from "../repository/educacaoRep";

export default {

    get : async (req: Request, res: Response) => {
        const data = findAll();
        return res.status(200).json({ quantidade: data.length ,dados: data })
    },

    getFiltros : async (req: Request, res: Response) => {
        const {municipio} = req.query; 
        const data = findMunicipio(municipio);
        return res.status(200).json({ quantidade: data.length ,dados: data })
    },

}

