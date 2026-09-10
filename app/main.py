from fastapi import FastAPI
from app.api.router import api_router

app = FastAPI(
    title="My API",
    version="1.0.0",
)

app.include_router(
    prefix="/api/v1",
    router=api_router,
)