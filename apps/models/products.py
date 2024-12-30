from django.db.models import Model, CharField, FloatField, ForeignKey, CASCADE, TextField


class Category(Model):
    title = CharField(max_length=255)

    def __str__(self):
        return self.title


class Product(Model):
    name = CharField(max_length=255)
    price = FloatField()
    category = ForeignKey('apps.Category', on_delete=CASCADE)
    description = TextField(max_length=500)

    def __str__(self):
        return self.name
