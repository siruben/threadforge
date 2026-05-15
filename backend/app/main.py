from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import upload, conversion

app = FastAPI(title="ThreadForge API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(upload.router, prefix="/api", tags=["upload"])
app.include_router(conversion.router, prefix="/api", tags=["conversion"])

@app.get("/")
async def root():
    return {"message": "ThreadForge API"}
