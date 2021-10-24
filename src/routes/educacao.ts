import { Router } from "express";
import educacaoContrller from "../controllers/educacao";

const routes = Router();

routes.get("/educacao", educacaoContrller.get)
routes.get("/educacao/filtro", educacaoContrller.getFiltros)

export default routes;
