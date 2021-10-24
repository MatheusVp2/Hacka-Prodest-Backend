import { Request, Response } from 'express';
import { findAll } from "../repository/educacaoRep";

export default {

    get : async (req: Request, res: Response) => {
        const data = findAll();
        return res.status(200).json({ quantidade: data.length ,dados: data })
    },

    post : async (req: Request, res: Response) => {

        return res.status(200).json({ ok: true})
    }

}

