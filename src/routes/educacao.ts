import { Router } from "express";
import educacaoContrller from "../controllers/educacao";

const routes = Router();

routes.get("/educacao", educacaoContrller.get)

export default routes;
