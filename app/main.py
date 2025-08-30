from fastapi import FastAPI

app = FastAPI(title="FastAPI starter")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/hello/{name}")
def hello(name: str):
    return {"message": f"hello, {name}"}