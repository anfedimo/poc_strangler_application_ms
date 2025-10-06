"""
Microservicio de usuarios para la arquitectura Strangler.
Provee endpoints relacionados con la gestión de usuarios.
"""

from fastapi import FastAPI

# Instancia principal de la aplicación FastAPI para usuarios
app = FastAPI()

@app.get("/usuarios")
def get_usuarios():
    """
    Endpoint para obtener la lista de usuarios.
    
    Returns:
        list: Lista de diccionarios con información de usuarios.
    """
    # Retorna una lista de usuarios de ejemplo
    return [{"id": 1, "nombre": "Fercho"}]