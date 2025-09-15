from fastapi import FastAPI

app = FastAPI(title="Weather Adapter API", version="0.1.0")
@app.get("/health")
def health():
    return {"ok": True}