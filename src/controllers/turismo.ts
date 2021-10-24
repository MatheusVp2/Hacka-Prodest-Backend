import { Request, Response, Router } from 'express';
import { findAll,findMunicipio } from "../repository/turismoRep";
export default {
    get: async (req: Request, res: Response) => {
        const {tipoTurismo} = req.params
        const data = findAll(tipoTurismo);
        return res.status(200).json({ quantidade: data.length ,dados: data })
    },

    getFiltro : async (req: Request, res: Response) => {
        const {municipio} = req.query;
        const {tipoTurismo} = req.params 
        const data = findMunicipio(municipio,tipoTurismo);
        return res.status(200).json({ quantidade: data.length ,dados: data })
    },

}