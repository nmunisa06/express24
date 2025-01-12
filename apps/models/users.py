from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, TextChoices, TextField


class User(AbstractUser):
    first_name = CharField(max_length=255, null=True, blank=True)
    phone = CharField(max_length=50, unique=True)
    street_name = CharField(max_length=255, blank=True, null=True)
    house_numb = CharField(max_length=75, blank=False)
    apartment_numb = CharField(max_length=75, blank=False)

    class Type(TextChoices):
        admin = 'admin', 'Admin'
        courier = 'courier', 'Courier'

    def __str__(self):
        return self.first_name
