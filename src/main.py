from typing import Union
from fastapi import FastAPI

from src.core.db.db import init_database, shutdown_database
from src.core.schemas.AppUser import AppUser
from src.core.settings import settings


app = FastAPI()

@app.on_event("startup")
async def init_config():
    init_database()

@app.on_event("shutdown")
async def shutdown():
    shutdown_database()

@app.get('/')
def index():
    return {
        'api_version': 'v1'
    }

@app.get('/info')
def info():
    return {
        'app_name': settings.app_name
    }
