from typing import Union
from fastapi import FastAPI
from mangum import Mangum
from starlette.middleware.sessions import SessionMiddleware

from src.core.settings import settings
from src.core.db.db import init_database, shutdown_database
from src.api.v1.auth import auth_router
from src.api.v1.info import info_router
from src.api.v1.lessons import lessons_router

app = FastAPI()

# app.add_middleware(SessionMiddleware, secret_key="some-random", https_only=True)

# app.include_router(auth_router)
# app.include_router(info_router)
# app.include_router(lessons_router)


@info_router.get('/v1/info')
async def info():
    return {
        'app_name': settings.app_name
    }

@info_router.get('/')
async def index():
    return {
        'api_version': 'v1'
    }

@app.on_event("startup")
async def init_config():
    init_database()


@app.on_event("shutdown")
async def shutdown():
    shutdown_database()

handler = Mangum(app=app)
