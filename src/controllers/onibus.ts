import { Request, Response } from 'express';
import { findAll } from "../repository/onibusRep";

export default {

    get : async (req: Request, res: Response) => {
        const data = findAll();
        return res.status(200).json({ quantidade: data.length ,dados: data })
    },
}