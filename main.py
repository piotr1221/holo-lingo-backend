from typing import Union
from fastapi import FastAPI
from mangum import Mangum

from src.core.db.db import init_database, shutdown_database
from src.core.schemas.AppUser import AppUser
from src.core.settings import settings

import json


from src.api.v1.contracts.register import UserPost

app = FastAPI()

@app.on_event("startup")
async def init_config():
    init_database()

@app.on_event("shutdown")
async def shutdown():
    shutdown_database()

@app.get('/')
async def index():
    return {
        'api_version': 'v1'
    }

@app.get('/info')
async def info():
    return {
        'app_name': settings.app_name
    }

########################## ENTIDAD USUARIO #############################

#CREATE
@app.post('/user')
def create_user(user: UserPost):
    new_user = AppUser(name=user.name, password=user.password)
    new_user.save()
    return {
        'message': "succesful operation"
    }

#READ
@app.get('/user')
def get_users():
    return json.loads(AppUser.objects().to_json())

@app.get('/user/info/{user_id}')
def get_user(user_id: str):
    return json.loads(AppUser.objects(id=user_id).first().to_json())

########################################################################

handler = Mangum(app=app)