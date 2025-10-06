from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from datetime import datetime
from database import get_db
from registro import Registro as RegistroDB

router = APIRouter(prefix="/bitacora", tags=["Bitácora"])

# Modelo Pydantic para entrada
class RegistroEntrada(BaseModel):
    nombre: str
    conviccion: float
    defensa: float
    roi: float
    tiempo_restante: datetime

@router.post("/registrar")
def registrar_senal(registro: RegistroEntrada, db: Session = Depends(get_db)):
    nuevo_registro = RegistroDB(
        nombre=registro.nombre,
        conviccion=registro.conviccion,
        defensa=registro.defensa,
        roi=registro.roi,
        created_at=datetime.now()
    )
    db.add(nuevo_registro)
    db.commit()
    db.refresh(nuevo_registro)
    return {"mensaje": "Señal registrada exitosamente", "id": nuevo_registro.id}

@router.get("/historial")
def historial(db: Session = Depends(get_db)):
    registros = db.query(RegistroDB).order_by(RegistroDB.created_at.desc()).all()
    return {"bitacora": [r.__dict__ for r in registros]}
