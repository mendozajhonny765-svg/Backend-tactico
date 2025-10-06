from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import Optional, List
from sqlalchemy.orm import Session
from datetime import datetime

from database import get_db
from registro import Registro as RegistroDB

router = APIRouter(prefix="/defensa", tags=["Defensa"])

class Contexto(BaseModel):
    nombre: str
    narrativa: Optional[float] = None
    fatiga: Optional[float] = None
    presion_laboral: Optional[float] = None
    presion_emocional: Optional[float] = None
    blindaje: Optional[float] = None
    conviccion: Optional[float] = None
    roi: Optional[float] = None

@router.post("/evaluar")
def evaluar_defensa(contexto: Contexto, db: Session = Depends(get_db)):
    alertas: List[str] = []

    if contexto.narrativa and contexto.narrativa > 0.5:
        alertas.append("Narrativa de obligación detectada")
    if contexto.fatiga and contexto.fatiga > 0.7:
        alertas.append("Fatiga elevada")
    if contexto.presion_laboral and contexto.presion_laboral > 0.6:
        alertas.append("Presión laboral elevada")
    if contexto.presion_emocional and contexto.presion_emocional > 0.6:
        alertas.append("Presión emocional elevada")

    # Registrar en bitácora si hay alertas
    if alertas:
        nuevo_registro = RegistroDB(
            nombre=contexto.nombre,
            conviccion=contexto.conviccion or 0.0,
            roi=contexto.roi or 0.0,
            defensa=contexto.blindaje or 0.0,
            created_at=datetime.now()
        )
        db.add(nuevo_registro)
        db.commit()
        db.refresh(nuevo_registro)

    return {
        "blindaje": contexto.blindaje,
        "alertas": alertas,
        "registrado": bool(alertas)
    }
