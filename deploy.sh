#!/bin/bash

echo "🔄 Desplegando nueva versión..."

# Activar entorno virtual
source venv/bin/activate

# Obtener los últimos cambios
sudo -i -u ubuntu bash -c 'cd /home/ubuntu/api-riesgo-penalizaciones && git pull origin main'

# Matar proceso Flask anterior (si lo hay)
pkill -f run.py

# Iniciar de nuevo en segundo plano
nohup python run.py > flask.log 2>&1 &

echo "✅ Despliegue completado y Flask reiniciado."

