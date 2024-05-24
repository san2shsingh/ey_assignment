 # app/main.py
from fastapi import FastAPI
from app.controllers.addition_controller import router as addition_router

app = FastAPI()

app.include_router(addition_router, prefix="/api/v1/addition")
