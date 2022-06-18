from src.api.v1.contracts.lesson import LessonPost
from src.core.schemas.Lessons import Lesson
from fastapi import APIRouter
from src.core.settings import settings

lessons_router = APIRouter()


@lessons_router.get('/lessons/search/{term}')
async def get_lessons(term):
    return {
        'message': 'obtener lecciones'
    }

@lessons_router.post('/lessons/create')
async def post_lessons(lesson: LessonPost):
    print(lesson)
    new_lesson=Lesson(title=lesson.title,description=lesson.description,example_video=lesson.example_video,category_name=lesson.category_name)
    new_lesson.save()
    return {
        'message':"Lesson saved successfully"
    }