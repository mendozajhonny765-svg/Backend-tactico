Creación de README.md para descripción del backend táctico# ⚔️ Sistema Táctico Predictivo

API modular para simulación, defensa, radar y aprendizaje.  
Desarrollado con **FastAPI** y **SQLAlchemy**, optimizado para despliegue en **Render**.

## 🚀 Endpoints principales

- `GET /simulador` → Simulación táctica  
- `GET /radar` → Escaneo de señales y momentum  
- `POST /defensa` → Activación de lógica defensiva  
- `POST /aprendizaje` → Registro y evolución predictiva

## 🧠 Arquitectura

- Modular por componentes (`simulador.py`, `radar.py`, etc.)  
- Integración con base de datos (`database.py`)  
- Configuración de dependencias en `requirements.txt`  
- Punto de entrada: `main.py`

## 📦 Despliegue

Compatible con Render:  
```bash
uvicorn main:app --host=0.0.0.0 --port=10000
