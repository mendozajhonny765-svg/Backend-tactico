from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# Configurar CORS para permitir conexión desde frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambiar por tu dominio si lo tienes
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers
from simulador import router as simulador_router
from bitacora import router as bitacora_router
from demo import router as demo_router

app.include_router(simulador_router)
app.include_router(bitacora_router)
app.include_router(demo_router)
# Importar routers
from simulador import señal_simular, bitacora, defensa, radar, aprendizaje

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

