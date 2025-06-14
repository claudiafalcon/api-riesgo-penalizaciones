from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="API Riesgo Penalizaciones")

app.include_router(router)

