"""
Microservicio de productos para la arquitectura Strangler.
Provee endpoints relacionados con la gestión de productos.
"""

from fastapi import FastAPI

# Instancia principal de la aplicación FastAPI para productos
app = FastAPI()

@app.get("/productos")
def get_productos():
    """
    Endpoint para obtener la lista de productos.
    
    Returns:
        list: Lista de diccionarios con información de productos.
    """
    # Retorna una lista de productos de ejemplo
    return [{"id": 1, "producto": "Carro"}]