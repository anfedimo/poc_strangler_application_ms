from fastapi import FastAPI, Request
import httpx

app = FastAPI()

MICROSERVICES = {
    "usuarios": "http://usuarios_service:8000",
    "pedidos": "http://pedidos_service:8000",
    "productos": "http://productos_service:8000",
}

@app.api_route("/{service}/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def proxy(service: str, path: str, request: Request):
    if service not in MICROSERVICES:
        return {"error": "Service not found"}
    url = f"{MICROSERVICES[service]}/{service}/{path}"
    async with httpx.AsyncClient() as client:
        response = await client.request(
            method=request.method,
            url=url,
            headers=dict(request.headers),
            data=await request.body()
        )
    return response.json()