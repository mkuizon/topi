# backend/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
load_dotenv()

app = FastAPI(
    title="topi backend",
    description="Backend API for the topi productivity platform",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {"message": "Hello from TOPI backend!!"}