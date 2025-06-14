from fastapi import APIRouter, Query
from app.services.s3 import list_files_by_day

router = APIRouter()

@router.get("/archivos")
def archivos_disponibles(tipo: str = Query("json")):
    return list_files_by_day(tipo)
