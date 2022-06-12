from dotenv import load_dotenv
import os

load_dotenv()

# class Settings(BaseSettings):
#     app_name : str
#     db_name: str
#     db_port: int
#     db_host : str
#     db_user : str
#     db_password: str
#     class Config:
#         env_file = '.env'
#         env_file_enconding = 'utf-8'

class Settings():

    def __init__(self):
        self.app_name = os.environ['APP_NAME']
        self.db_name = os.environ['DB_NAME']
        self.db_port = int(os.environ['DB_PORT'])
        self.db_host = os.environ['DB_HOST']
        self.db_user = os.environ['DB_USER']
        self.db_password = os.environ['DB_PASSWORD']
        # self.app_name = 'xd'

settings = Settings()