from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name : str
    db_name: str
    port: int
    host : str
    class Config:
        env_file = '.env'
        env_file_enconding = 'utf-8'

settings = Settings()