from fastapi import Header, HTTPException

# Define aquí tu API key (puede venir luego de variable de entorno si quieres)
API_KEY = "mi-token-secreto"

def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Unauthorized")