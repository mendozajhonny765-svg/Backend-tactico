from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

router = APIRouter(prefix="/aprendizaje", tags=["Aprendizaje"])

class Ajuste(BaseModel):
    parametro: str
    valor: float
    contexto: Optional[str] = None

ajustes_db = {}

@router.post("/ajustar")
def ajustar_parametro(ajuste: Ajuste):
    ajustes_db[ajuste.parametro] = ajuste.valor
    respuesta = {"mensaje": f"Parámetro '{ajuste.parametro}' ajustado a {ajuste.valor}"}

    if ajuste.contexto:
        respuesta["contexto"] = ajuste.contexto

    return respuesta

@router.get("/estado")
def estado_actual():
    return {"ajustes": ajustes_db}