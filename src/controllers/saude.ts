import { Request, Response } from 'express';

export default {

    get : async (req: Request, res: Response) => {

        return res.status(200).json({ ok: true})
    },

    post : async (req: Request, res: Response) => {

        return res.status(200).json({ ok: true})
    }

}

