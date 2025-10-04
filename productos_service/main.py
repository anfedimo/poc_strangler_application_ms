from fastapi import FastAPI

app = FastAPI()

@app.get("/productos")
def get_productos():
    return [{"id": 1, "producto": "Carro"}]