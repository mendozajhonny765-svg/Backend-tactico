from sqlalchemy import Column, String, Float, DateTime, Integer
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Ajuste(Base):
    __tablename__ = "ajustes"

    id = Column(Integer, primary_key=True, index=True)
    parametro = Column(String, index=True)
    valor = Column(Float)
    contexto = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.now)
