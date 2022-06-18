from fastapi import APIRouter
from src.core.settings import settings

info_router =APIRouter()

@info_router.get('/')
async def index():
    return {
        'api_version': 'v1'
    }

@info_router.get('/info')
async def info():
    return {
        'app_name': settings.app_name
    }