"""
Microservicio de pedidos para la arquitectura Strangler.
Provee endpoints relacionados con la gestión de pedidos.
"""

from fastapi import FastAPI

# Instancia principal de la aplicación FastAPI para pedidos
app = FastAPI()

@app.get("/pedidos")
def get_pedidos():
    """
    Endpoint para obtener la lista de pedidos.
    
    Returns:
        list: Lista de diccionarios con información de pedidos.
    """
    # Retorna una lista de pedidos de ejemplo
    return [{"id": 1, "pedido": "Del carro para el grupo 14"}]