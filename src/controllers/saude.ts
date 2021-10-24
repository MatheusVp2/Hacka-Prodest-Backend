import { Request, Response } from 'express';
import { findAll,findMunicipio } from "../repository/saudeRep";

export default {

    get : async (req: Request, res: Response) => {
        const data =  findAll()
        return res.status(200).json({ quantidade: data.length ,dados: data})
    },
    getFiltro: async (req: Request, res: Response) => {
        const {municipio} = req.query
        const data =  findMunicipio(municipio)
        return res.status(200).json({ quantidade: data.length ,dados: data})
    },
    post : async (req: Request, res: Response) => {
        return res.status(200).json({ ok: true})
    }

}

