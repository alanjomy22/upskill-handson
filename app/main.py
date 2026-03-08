from fastapi import FastAPI
from app.config import settings

app = FastAPI(
    title="E-Commerce API",
    description="Backend API for e-commerce platform",
    version="1.0.0",
)

@app.on_event("startup")
async def startup_event():
    print(f"🚀 Server starting in {settings.APP_ENV} mode on port {settings.PORT}")