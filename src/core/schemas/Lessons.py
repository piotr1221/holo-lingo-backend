from mongoengine import *
import datetime as dt

class Lesson(Document):
    title = StringField(required=True,max_length=100)
    description=StringField(max_length=255)
    example_video=StringField(max_length=255)
    date_created = DateTimeField(default=dt.datetime.utcnow,help_text='date the user was created')


class Category(Document):
  name= StringField(requider=True,max_length=100)
