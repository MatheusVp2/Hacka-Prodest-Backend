import { Router } from "express";
import onibusContrller from "../controllers/onibus";

const routes = Router();

routes.get("/pontosOnibus", onibusContrller.get)
export default routes;