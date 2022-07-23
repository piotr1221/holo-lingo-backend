from email.policy import default
from xmlrpc.client import DateTime
from mongoengine import *
import datetime as dt
from src.core.schemas.AppUser import AppUser


class Lesson(Document):
    title = StringField(required=True,max_length=100)
    description=StringField(max_length=255)
    example_video=StringField(max_length=255)
    date_created = DateTimeField(default=dt.datetime.utcnow,help_text='date the user was created')
    category_name=StringField(max_length=50)

class Grade(Document):
    user_id=ReferenceField(AppUser)
    lesson_id=ReferenceField(Lesson)
    grade=DecimalField(min_value=0,max_value=100)
    completed=BooleanField(default=False)
    date_created=DateTimeField(default=dt.datetime.utcnow,help_text='date the user was created')