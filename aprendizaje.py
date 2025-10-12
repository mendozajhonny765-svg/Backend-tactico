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
    cuota: Optional[float] = None
    deporte: Optional[str] = "otros"

def activar_senal_apuesta(parametro, valor, cuota, contexto, deporte):
    criterios = {
        "futbol": {"valor_min": 0.85, "cuota_max": 2.5},
        "tenis": {"valor_min": 0.80, "cuota_max": 2.8},
        "baloncesto": {"valor_min": 0.78, "cuota_max": 2.6},
        "otros": {"valor_min": 0.82, "cuota_max": 2.7}
    }

    config = criterios.get(deporte.lower(), criterios["otros"])

    if valor >= config["valor_min"] and (cuota is not None and cuota <= config["cuota_max"]):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        mensaje = f"""
        🔔 SEÑAL DE APUESTA ACTIVADA 🔔
        🕒 Hora: {timestamp}
        🏟️ Deporte: {deporte.upper()}
        🎯 Parámetro: {parametro}
        📊 Valor: {valor}
        💸 Cuota: {cuota}
        📌 Contexto: {contexto}
        """
        print(mensaje)
        return True
    return False

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

    señal_activada = activar_senal_apuesta(
        parametro=ajuste.parametro,
        valor=ajuste.valor,
        cuota=ajuste.cuota,
        contexto=ajuste.contexto or "Sin contexto",
        deporte=ajuste.deporte
    )

    return {
        "mensaje": f"Parámetro '{ajuste.parametro}' ajustado a {ajuste.valor}",
        "id": nuevo_ajuste.id,
        "señal_activada": señal_activada
    }

@router.get("/estado")
def estado_actual(db: Session = Depends(get_db)):
    ajustes = db.query(AjusteDB).order_by(AjusteDB.created_at.desc()).all()
    return {"ajustes": [a.__dict__ for a in ajustes]}
