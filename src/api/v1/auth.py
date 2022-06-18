from fastapi import APIRouter
from src.core.settings import settings
from src.core.schemas.AppUser import AppUser
from src.api.v1.contracts.register import UserPost
import json

auth_router =APIRouter()

@auth_router.post('/user')
def create_user(user: UserPost):
    new_user = AppUser(name=user.name, password=user.password)
    new_user.save()
    return {
        'message': "succesful operation"
    }

@auth_router.get('/user')
def get_users():
    return json.loads(AppUser.objects().to_json())