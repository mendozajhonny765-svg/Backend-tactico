from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import Optional
from sqlalchemy.orm import Session
from datetime import datetime

from database import get_db
from registro import Ajuste as AjusteDB  # O desde modelos.py si lo separas

router = APIRouter(prefix="/aprendizaje", tags=["Aprendizaje"])

class AjusteEntrada(BaseModel):
    parametro: str
    valor: float
    contexto: Optional[str] = None

@router.post("/ajustar")
def ajustar_parametro(ajuste: AjusteEntrada, db: Session = Depends(get_db)):
    nuevo_ajuste = AjusteDB(
        parametro=ajuste.parametro,
        valor=ajuste.valor,
        contexto=ajuste.contexto or "",
        created_at=datetime.now()
    )
    db.add(nuevo_ajuste)
    db.commit()
    db.refresh(nuevo_ajuste)

    return {
        "mensaje": f"Parámetro '{ajuste.parametro}' ajustado a {ajuste.valor}",
        "id": nuevo_ajuste.id
    }

@router.get("/estado")
def estado_actual(db: Session = Depends(get_db)):
    ajustes = db.query(AjusteDB).order_by(AjusteDB.created_at.desc()).all()
    return {"ajustes": [a.__dict__ for a in ajustes]}
