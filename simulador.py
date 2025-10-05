from fastapi import APIRouter, Query
from pydantic import BaseModel
from typing import Optional

router = APIRouter(prefix="/simular", tags=["Simulador"])

class Señal(BaseModel):
    partido: str
    cuota: float
    probabilidad: float
    contexto: Optional[str] = None

@router.post("/")
def simular_senal(senal: Señal):
    conviccion = round(senal.probabilidad * senal.cuota, 2)
    riesgo = round((1 - senal.probabilidad) * senal.cuota, 2)
    roi = round((senal.probabilidad * senal.cuota - 1) * 100, 2)

    defensa = "Activada" if senal.contexto and "riesgo" in senal.contexto.lower() else "Pasiva"

    return {
        "partido": senal.partido,
        "cuota": senal.cuota,
        "probabilidad": senal.probabilidad,
        "conviccion": conviccion,
        "riesgo": riesgo,
        "roi": f"{roi}%",
        "defensa": defensa
    }