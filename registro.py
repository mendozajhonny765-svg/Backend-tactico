from sqlalchemy import Column, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class Registro(Base):
    __tablename__ = "registros"

    id = Column(String, primary_key=True, index=True)
    partido = Column(String)
    conviccion = Column(Float)
    roi = Column(Float)
    defensa = Column(String)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)