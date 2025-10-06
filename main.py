from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Importar routers de cada módulo
from simulador import router as simulador_router
from defensa import router as defensa_router
from bitacora import router as bitacora_router
from aprendizaje import router as aprendizaje_router
# Si tienes radar o sistema_tactico_predictivo, agrégalos aquí también

app = FastAPI(title="Sistema Táctico Predictivo")

# Configurar CORS para permitir acceso desde cualquier origen
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers
app.include_router(simulador_router)
app.include_router(defensa_router)
app.include_router(bitacora_router)
app.include_router(aprendizaje_router)

# Endpoint raíz
@app.get("/")
def root():
    return {"mensaje": "Sistema Táctico Predictivo operativo"}

# Endpoint de estado
@app.get("/status")
def status():
    return {"estado": "activo", "modulos": ["simulador", "defensa", "bitacora", "aprendizaje"]}

# Ejecutar con Uvicorn si se lanza directamente
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=10000)
