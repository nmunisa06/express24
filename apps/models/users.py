from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, Model


class User(Model):
    first_name = CharField(max_length=255, null=True, blank=True)
    last_name = CharField(max_length=255)

