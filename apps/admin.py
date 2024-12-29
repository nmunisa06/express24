from django.contrib import admin

from apps.models.products import Product, Category
from apps.models.users import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    ...

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    ...

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...
