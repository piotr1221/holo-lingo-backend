from fastapi import APIRouter
from src.core.settings import settings

lessons_router = APIRouter()


@lessons_router.get('/lessons/search/{term}')
async def get_lessons(term):
    return {
        'message': 'obtener lecciones'
    }
