from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from hive import BrillianceHive

app = FastAPI(title="Brilliance Hive v5.2")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

hive = BrillianceHive()

app.mount("/static", StaticFiles(directory="../frontend/dist", html=True), name="static")

@app.get("/api/status")
async def status():
    return hive.get_status()

@app.post("/api/think")
async def think(request: dict):
    return hive.think(request.get("stimulus", ""))

@app.get("/")
async def root():
    return {"message": "Brilliance Hive v5.2 - Sovereign & Alive"}