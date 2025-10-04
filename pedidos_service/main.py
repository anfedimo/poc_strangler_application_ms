from fastapi import FastAPI

app = FastAPI()

@app.get("/pedidos")
def get_pedidos():
    return [{"id": 1, "pedido": "Del carro para el grupo 14"}]