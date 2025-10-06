from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

# Obtener la URL de la base de datos desde variables de entorno
DATABASE_URL = os.getenv("DATABASE_URL")

# Crear el motor de conexión
engine = create_engine(DATABASE_URL, echo=True)  # echo=True para ver consultas SQL en logs

# Crear la sesión local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Función para obtener la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
