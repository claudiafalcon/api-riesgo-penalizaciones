from fastapi import APIRouter, Query, Depends, HTTPException, Header
from app.services.s3 import list_files_by_day, generate_presigned_url, list_presigned_urls_for_day
from app.utils.auth import verify_api_key

router = APIRouter()


@router.get("/")
def root():
    return {"message": "API de Riesgo Penalizaciones operando ✅"}

@router.get("/archivos")
def archivos_disponibles(tipo: str = Query("parquet")):
    return list_files_by_day(tipo)



@router.get("/descarga")
def get_urls_for_day(
    file: str = Query(..., description="Ruta tipo 'transactionresponse/day=01-05-2025'"),
    tipo: str = Query("parquet", regex="^(json|parquet)$"),
    auth: None = Depends(verify_api_key)
):
    urls = list_presigned_urls_for_day(file, tipo)
    if not urls:
        return {"error": "No se encontraron archivos"}
    return {"urls": urls}


@router.get("/descarga-multiple")
def descargar_por_rango(
    coleccion: str,
    tipo: str = Query("parquet"),
    inicio: str = Query(...),  # formato YYYY-MM-DD
    fin: str = Query(...)
):
    return generate_presigned_urls_by_range(coleccion, tipo, inicio, fin)