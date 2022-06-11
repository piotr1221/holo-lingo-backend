from mongoengine import connect, disconnect
from core.settings import settings

def init_database():
    connect(
        db=settings.db_name,
        username='root',
        password='password',
        host=settings.host,
        port=settings.port,
    )
    pass

def shutdown_database():
    disconnect()