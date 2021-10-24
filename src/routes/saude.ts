import { Router } from "express";
import saudeController from "../controllers/saude";

const routes = Router();

routes.get("/saude", saudeController.get)
routes.get("/saude/filtro", saudeController.getFiltro)

export default routes;
