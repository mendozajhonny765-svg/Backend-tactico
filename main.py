from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Importar routers
from app.routers import simulador, bitacora, defensa, radar, aprendizaje

app = FastAPI(
    title="Sistema Táctico Predictivo",
    description="API para simulación, defensa, registro y aprendizaje táctico en tiempo real",
    version="1.0.0"
)

# Configurar CORS para permitir conexión desde frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambiar por tu dominio en producción
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers
app.include_router(simulador.router)
app.include_router(bitacora.router)
app.include_router(defensa.router)
app.include_router(radar.router)
app.include_router(aprendizaje.router)

# Endpoint raíz opcional
@app.get("/")
def root():
    return {"mensaje": "Sistema táctico operativo"}