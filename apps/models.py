from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, TextChoices


class User(AbstractUser):
    first_name = CharField(max_length=255, null=True, blank=True)
    phone = CharField(max_length=50, unique=True)

    class Type(TextChoices):
        admin = 'admin', 'Admin'
        courier = 'courier', 'Courier'

    def __str__(self):
        return self.first_name
