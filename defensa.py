from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

router = APIRouter(prefix="/defensa", tags=["Defensa"])

class Contexto(BaseModel):
    partido: str
    narrativa: Optional[str] = None
    fatiga: Optional[float] = None
    presion: Optional[str] = None

@router.post("/evaluar")
def evaluar_defensa(ctx: Contexto):
    blindaje = "Pasivo"
    alerta = []

    if ctx.narrativa and "obligado" in ctx.narrativa.lower():
        blindaje = "Activo"
        alerta.append("Narrativa de obligación detectada")

    if ctx.fatiga and ctx.fatiga > 0.7:
        blindaje = "Activo"
        alerta.append("Fatiga elevada")

    if ctx.presion and "emocional" in ctx.presion.lower():
        blindaje = "Activo"
        alerta.append("Presión emocional detectada")

    return {
        "partido": ctx.partido,
        "blindaje": blindaje,
        "alertas": alerta
    }