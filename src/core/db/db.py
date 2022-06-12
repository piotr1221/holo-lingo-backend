from mongoengine import connect, disconnect
from ..schemas.AppUser import AppUser
from ..settings import settings

def init_database():
    connect(
        db=settings.db_name,
        username=settings.db_user,
        password=settings.db_password,
        host=settings.db_host,
        port=settings.db_port,
    )
    pass

def shutdown_database():
    disconnect()