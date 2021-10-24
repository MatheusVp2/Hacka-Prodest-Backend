import { Router } from "express";
import turismoController from "../controllers/turismo";

const routes = Router();
routes.get("/turismo/:tipoTurismo", turismoController.get)
routes.get("/turismo/:tipoTurismo/filtro", turismoController.getFiltro)

export default routes;