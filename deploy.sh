#!/bin/bash

echo "🔄 Desplegando nueva versión..."

# Activar entorno virtual
source venv/bin/activate

# Obtener los últimos cambios
sudo -i -u ubuntu bash -c 'cd /home/ubuntu/api-riesgo-penalizaciones && git pull origin main'

# Matar procesos uvicorn anteriores (si lo hay)
pkill -f "uvicorn main:app"

# Iniciar FastAPI en segundo plano
nohup uvicorn main:app --host 0.0.0.0 --port 8000 > fastapi.log 2>&1 &

echo "✅ Despliegue completado y FastAPI reiniciado."