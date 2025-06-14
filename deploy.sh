#!/bin/bash

echo "🔄 Desplegando nueva versión..."

cd ~/api-riesgo-penalizaciones

# Crear entorno virtual si no existe
if [ ! -d "venv" ]; then
  echo "📦 Creando entorno virtual..."
  python3 -m venv venv
fi

# Activar entorno virtual
source venv/bin/activate

# Obtener los últimos cambios
git pull origin main

# Instalar dependencias
echo "📚 Instalando dependencias..."
pip install --upgrade pip
pip install -r requirements.txt

# Matar proceso anterior si existe
pkill -f "uvicorn app.main:app"

# Lanzar FastAPI en segundo plano y guardar log
echo "🚀 Iniciando FastAPI..."
nohup python3 -m uvicorn app.main:app --host 0.0.0.0 --port 8000 > fastapi.log 2>&1 &

echo "✅ Despliegue completado y FastAPI reiniciado."