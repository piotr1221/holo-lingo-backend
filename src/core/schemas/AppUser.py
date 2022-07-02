from mongoengine import *
import datetime as dt
from passlib.hash import pbkdf2_sha256

class AppUser(Document):
    name = StringField(required=True,max_length=128)
    password = StringField(required=True)
    date_created = DateTimeField(default=dt.datetime.utcnow,help_text='date the user was created')
    issuer=StringField(required=True,max_length=256)
    email=StringField(required=True, max_length=128, unique=True)

    def save(self, *args, **kwargs):
        self.password = pbkdf2_sha256.hash(self.password)
        super(AppUser, self).save(*args, **kwargs)
        
    def val_password(self, out_password: str):
        return pbkdf2_sha256.hash(out_password,self.password)