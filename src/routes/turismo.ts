import { Router } from "express";
import turismoController from "../controllers/turismo";

const routes = Router();
routes.get("/turismo", turismoController.get)
routes.get("/turismo/filtro", turismoController.getFiltros)
export default routes;