# Imagen base de Python optimizada y ligera
FROM python:3.12-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo principal de la aplicación al contenedor
COPY main.py .

# Instala las dependencias necesarias para ejecutar FastAPI y el proxy HTTP
RUN pip install fastapi uvicorn httpx

# Expone el puerto 8000 para acceder al API Gateway desde fuera del contenedor
EXPOSE 8000

# Comando por defecto para iniciar el servidor Uvicorn con la aplicación FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]