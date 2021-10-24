import { Router } from "express";
import segurancaController from "../controllers/seguranca";

const routes = Router();

routes.get("/seguranca", segurancaController.get)
routes.get("/seguranca/filtro", segurancaController.getFiltro)

export default routes;
