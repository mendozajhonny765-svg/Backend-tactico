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
    
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

router = APIRouter(prefix="/defensa", tags=["defensa"])

class Contexto(BaseModel):
    partido: str
    narrativa: Optional[str] = None
    alerta: Optional[str] = None
    falta: Optional[float] = None
    obligacion: Optional[float] = None

@router.post("/evaluar")
def evaluar_defensa(ctx: Contexto):
    alertas = []

    if ctx.narrativa and "obligado" in ctx.narrativa.lower():
        alertas.append("Narrativa de obligación detectada")

    return {
        "partido": ctx.partido,
        "alertas": alertas
    }

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
