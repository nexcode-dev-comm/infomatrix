import asyncio
from typing import List
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


import checkers
import db
import leakcheck
import schemas
import masker
import report

app = FastAPI(
    title="OSINT Digital Footprint Mapper API",
    description="Backend для поиска цифрового следа и утечек личных данных",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"status": "online", "message": "OSINT API приветствует тебя"}

