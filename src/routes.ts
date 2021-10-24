import { Router } from 'express'
const api_v1 = Router()

import routeEducacao from "./routes/educacao";
import routeSaude from "./routes/saude";
import routeSeguranca from "./routes/seguranca";

const routes_api_v1 = [
    routeEducacao,
    routeSaude,
    routeSeguranca
]

api_v1.use('/api/v1', ...routes_api_v1);

export { api_v1 }
