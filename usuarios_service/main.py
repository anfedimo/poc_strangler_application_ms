from fastapi import FastAPI

app = FastAPI()

@app.get("/usuarios")
def get_usuarios():
    return [{"id": 1, "nombre": "Fercho"}]