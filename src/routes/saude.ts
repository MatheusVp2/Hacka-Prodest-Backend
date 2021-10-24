import { Router } from "express";
import saudeController from "../controllers/saude";

const routes = Router();

routes.get("/saude", saudeController.get)

export default routes;
