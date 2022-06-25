from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get('/v1/info')
async def info():
    return {
        'app_name': 'aaaa'
    }

@app.get('/')
async def index():
    return {
        'api_version': 'v1'
    }

handler = Mangum(app=app)
