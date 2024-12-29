from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, Model, TextChoices


class User(Model):
    class Type(TextChoices):
        admin = 'admin', 'Admin'
        courier = 'courier', 'Courier'

    full_name = CharField(max_length=255, null=True, blank=True)
    phone = CharField(max_length=50, unique=True)

    def __str__(self):
        return self.full_name
