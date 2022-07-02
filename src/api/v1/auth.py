import email
from fastapi import APIRouter
from src.core.settings import settings
from src.core.schemas.AppUser import AppUser
from src.api.v1.contracts.auth import ClassicLoginUser, ClassicUserPost
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.responses import RedirectResponse
from src.core.oauth import oauth

from operator import attrgetter
import json
import requests

auth_router =APIRouter(prefix="/v1")

@auth_router.post('/register/email')
async def register_via_email(user: ClassicUserPost):
    new_user = AppUser(name=user.name, password=user.password, issuer="localhost", email=user.email)
    new_user.save()
    return attrgetter('name','email', 'issuer', 'date_created')(new_user)

@auth_router.post('/login/email')
async def login_via_email(user:ClassicLoginUser):
    target = AppUser.objects.get(email=user.email)
    if target is None: 
        return JSONResponse({
            'message': 'user not found'
        }, status_code=404)
    result = target.val_password(user.password)
    if result:
        return JSONResponse({
            'message': 'user authenticated'
        },status_code=200)
    else:
        return JSONResponse({
            'message': 'user no authenticated'
        }, status_code=401)


@auth_router.get('/user')
def get_users():
    return json.loads(AppUser.objects().to_json())

@auth_router.get('/login/google')
async def login_via_google(request: Request):
    redirect_uri = request.url_for('auth_via_google')
    return await oauth.google.authorize_redirect(request, redirect_uri)

@auth_router.get('/testapi')
async def test(request: Request):
    return request

@auth_router.get('/test', tags=['auth_required'])
async def home(request: Request):
    user = request.session.get('user')
    token = request.session.get('token')
    if user is not None and token is not None:
        return [user, token]
    return JSONResponse({ 'message': 'no user founded' }, status_code=401)

@auth_router.post('/logout')
async def logout(request: Request):
    request.session.clear()
    return JSONResponse({
        'message': 'successful operation'
    }, status_code=200)

@auth_router.get('/validate/google')
async def google_validate(request: Request):
    token = request.session.get('token')
    validate_url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?'
                    'access_token=%s' % token['access_token'])
    return requests.get(validate_url).json()

@auth_router.get('/refresh/google')
async def google_refresh_token(request : Request):
    token = request.session.get('token')
    temp = oauth.google(token=token['id_token'])
    return temp.refresh_token("https://accounts.google.com/o/oauth2/token")

@auth_router.get('/auth/google')
async def auth_via_google(request: Request):

    token = await oauth.google.authorize_access_token(request)
    
    user = token['userinfo']
    del token['userinfo']

    user_list = AppUser.objects(email=user.email)
    user_target = None
    if len(user_list) == 0 :
        user_target = AppUser(
            name=user.name,
            password='',
            email=user.email,
            issuer=user['iss'],
        )
        user_target.save()
    else:
        user_target = user_list.first()

    request.session['user'] = dict(user)
    request.session['token'] = dict(token)
    print(user_target)
    return RedirectResponse(request.url_for('home'))
    #return attrgetter('name','email', 'issuer', 'date_created')(new_user)

    
