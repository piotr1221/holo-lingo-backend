from mongoengine import *
import datetime as dt

class AppUser(Document):
    name = StringField(required=True,max_length=200)
    password = StringField(required=True)
    date_created = DateTimeField(default=dt.datetime.utcnow,help_text='date the user was created')