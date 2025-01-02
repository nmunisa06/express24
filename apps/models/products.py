from django.db.models import Model, CharField, FloatField, ForeignKey, CASCADE, TextField, ManyToManyField, \
    DateTimeField, ImageField, PositiveIntegerField


class Category(Model):
    title = CharField(max_length=255)

    def __str__(self):
        return self.title

class Product(Model):
    name = CharField(max_length=255)
    price = FloatField()
    description = TextField(max_length=500)
    image = ImageField(upload_to='productImage/', blank=True)
    category = ForeignKey('apps.Category', on_delete=CASCADE, blank=True)

    def __str__(self):
        return self.name


class Cart(Model):
    user_id = ForeignKey('apps.User', on_delete=CASCADE, blank=True)
    updated_at = DateTimeField(auto_now=True)
    created_at = DateTimeField(auto_now_add=True)
    Status_Choices = [
        ('pending', 'Pending'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]
    status = CharField(max_length=255, choices=Status_Choices, default='pending')

    def __str__(self):
        return f'Order: {self.created_at.strftime("%b %d %I:%M %p")}'


class CartItem(Model):
    quantity = PositiveIntegerField()
    cart_id = ForeignKey('apps.Cart', on_delete=CASCADE, related_name='items')
    product = ForeignKey('apps.Product', on_delete=CASCADE)
