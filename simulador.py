from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import Optional
from sqlalchemy.orm import Session
from database import get_db
from registro import Ajuste as AjusteDB

router = APIRouter(tags=["Simulador"])

class Senal(BaseModel):
    partido: str
    cuota: float
    probabilidad: float
    contexto: Optional[str] = None

def obtener_ajustes(db: Session):
    ajustes = db.query(AjusteDB).order_by(AjusteDB.created_at.desc()).all()
    modificadores = {}
    for ajuste in ajustes:
        modificadores[ajuste.parametro] = ajuste.valor
    return modificadores

@router.post("/senal")
def procesar_senal(senal: Senal, db: Session = Depends(get_db)):
    ajustes = obtener_ajustes(db)

    # Aplicar modificadores si existen
    probabilidad_mod = ajustes.get("probabilidad", 1.0)
    cuota_mod = ajustes.get("cuota", 1.0)
    defensa_mod = ajustes.get("defensa", 1.0)

    conviccion = (senal.probabilidad * probabilidad_mod) * (senal.cuota * cuota_mod)
    riesgo = (senal.cuota * cuota_mod) / (senal.probabilidad * probabilidad_mod)
    defensa = round((conviccion / riesgo) * defensa_mod, 2)

    return {
        "partido": senal.partido,
        "cuota": senal.cuota,
        "probabilidad": senal.probabilidad,
        "conviccion": round(conviccion, 2),
        "riesgo": round(riesgo, 2),
        "contexto": senal.contexto,
        "defensa": defensa,
        "ajustes_aplicados": ajustes
                   }
