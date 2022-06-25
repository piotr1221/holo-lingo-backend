from fastapi import APIRouter, Body
from src.core.settings import settings
from src.core.schemas.AppUser import AppUser
from src.api.v1.contracts.auth import ClassicUserPost, ModifyUserPost
from starlette.requests import Request
from src.core.oauth import oauth

from operator import attrgetter
import json


auth_router =APIRouter(prefix="/v1")

@auth_router.post('/login/email')
async def login_via_email(user: ClassicUserPost):
    new_user = AppUser(name=user.name, password=user.password, issuer="localhost", email=user.email)
    new_user.save()
    return attrgetter('name','email', 'issuer', 'date_created')(new_user)

@auth_router.get('/user')
def get_users():
    return json.loads(AppUser.objects().to_json())

@auth_router.get('/user/info')
def get_user(payload: dict=Body(...)):
    user_id = payload["id"]
    return json.loads(AppUser.objects(id=user_id).first().to_json())

@auth_router.patch('/user/edit')
def update_users(user: ModifyUserPost):
    modified_user = AppUser.objects(id=user.id).first()
    modified_user.name = user.name
    modified_user.save()
    user_json = json.loads(modified_user.to_json())
    return user_json

@auth_router.get('/login/google')
async def login_via_google(request: Request):
    redirect_uri = request.url_for('auth_via_google')
    return await oauth.google.authorize_redirect(request, redirect_uri)


@auth_router.get('/auth/google')
async def auth_via_google(request: Request):
    token = await oauth.google.authorize_access_token(request)
    user = token['userinfo']
    
    new_user = AppUser(
        name=user.name,
        password='',
        email=user.email,
        issuer=user.iss,
    )
    new_user.save()
    return attrgetter('name','email', 'issuer', 'date_created')(new_user)
