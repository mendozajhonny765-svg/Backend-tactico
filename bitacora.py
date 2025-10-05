from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from datetime import datetime

router = APIRouter(prefix="/bitacora", tags=["Bitácora"])

class Registro(BaseModel):
    partido: str
    conviccion: float
    roi: float
    defensa: str
    timestamp: datetime

bitacora_db: List[Registro] = []

@router.post("/registrar")
def registrar_senal(registro: Registro):
    bitacora_db.append(registro)
    return {"mensaje": "Señal registrada", "total_registros": len(bitacora_db)}

@router.get("/historial")
def obtener_historial():
    return {"bitacora": bitacora_db}