from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware 
from app.core.config import settings 
from app.core.database import engine 
from app.models.base import Base 
from app.api.v1 import beneficiaries 
 
# Create tables 
Base.metadata.create_all(bind=engine) 
 
app = FastAPI( 
    title=settings.APP_NAME, 
    version=settings.APP_VERSION, 
    description="Rural Livelihood & Skill Development Tracker API", 
    docs_url="/docs", 
    redoc_url="/redoc", 
    openapi_url="/openapi.json" 
) 
 
app.add_middleware( 
    CORSMiddleware, 
    allow_origins=settings.CORS_ORIGINS, 
    allow_credentials=settings.CORS_ALLOW_CREDENTIALS, 
    allow_methods=["*"], 
    allow_headers=["*"], 
) 
 
# Include routers 
app.include_router(beneficiaries.router, prefix="/api/v1") 
 
@app.get("/") 
async def root(): 
    return {"message": "Welcome to RLSD-Tracker API", "version": settings.APP_VERSION} 
 
@app.get("/health") 
async def health_check(): 
    return {"status": "healthy", "environment": settings.ENVIRONMENT} 
 
if __name__ == "__main__": 
    import uvicorn 
    uvicorn.run("app.main:app", host=settings.HOST, port=settings.PORT, reload=settings.RELOAD) 
