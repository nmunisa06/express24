from django.db.models import Model, CharField, FloatField, ForeignKey, CASCADE, TextField, ManyToManyField, \
    DateTimeField, ImageField


class Category(Model):
    title = CharField(max_length=255)

    def __str__(self):
        return self.title

class Product(Model):
    name = CharField(max_length=255)
    price = FloatField()
    category = ForeignKey('apps.Category', on_delete=CASCADE, blank=True)
    description = TextField(max_length=500)
    image = ImageField(upload_to='productImage/', blank=True)

    def __str__(self):
        return self.name

class OrderProduct(Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    price = FloatField()
    products = ManyToManyField('apps.Product', related_name='order', blank=True)
    Status_Choices = [
        ('pending', 'Pending'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]
    status = CharField(max_length=255, choices=Status_Choices, default='pending')

    def __str__(self):
        return f'Order: {self.created_at.strftime("%b %d %I:%M %p")}'

