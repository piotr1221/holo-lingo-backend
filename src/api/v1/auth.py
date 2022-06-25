from fastapi import APIRouter
from src.core.settings import settings
from src.core.schemas.AppUser import AppUser
from src.api.v1.contracts.auth import ClassicUserPost
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
