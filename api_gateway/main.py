"""
Módulo principal del API Gateway para la arquitectura Strangler.
Recibe peticiones y las reenvía al microservicio correspondiente.
"""

from fastapi import FastAPI, Request
import httpx

# Instancia principal de la aplicación FastAPI
app = FastAPI()

# Diccionario que mapea los nombres de los microservicios a sus URLs internas
MICROSERVICES = {
    "usuarios": "http://usuarios_service:8000",  # Microservicio de usuarios
    "pedidos": "http://pedidos_service:8000",    # Microservicio de pedidos
    "productos": "http://productos_service:8000",# Microservicio de productos
}

@app.api_route("/{service}/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def proxy(service: str, path: str, request: Request):
    """
    Proxy universal que recibe cualquier petición y la reenvía al microservicio adecuado.
    
    Args:
        service (str): Nombre del microservicio destino (usuarios, pedidos, productos).
        path (str): Ruta interna dentro del microservicio.
        request (Request): Objeto de la petición original.

    Returns:
        dict: Respuesta JSON del microservicio o error si el servicio no existe.
    """
    # Verifica si el microservicio solicitado existe
    if service not in MICROSERVICES:
        return {"error": "Service not found"}

    # Construye la URL destino usando el nombre del microservicio y la ruta
    url = f"{MICROSERVICES[service]}/{service}/{path}"

    # Reenvía la petición original al microservicio usando httpx
    async with httpx.AsyncClient() as client:
        response = await client.request(
            method=request.method,           # Método HTTP original (GET, POST, etc.)
            url=url,                         # URL destino
            headers=dict(request.headers),   # Cabeceras originales
            data=await request.body()        # Cuerpo de la petición original
        )
    # Devuelve la respuesta del microservicio como JSON
    return response.json()