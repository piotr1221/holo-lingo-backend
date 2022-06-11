from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name : str
    db_name: str
    db_port: int
    db_host : str
    db_user : str
    db_password: str
    class Config:
        env_file = '.env'
        env_file_enconding = 'utf-8'

settings = Settings()