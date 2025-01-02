from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.models.products import Product, Category
from apps.models.users import User


@admin.register(User)
class UserModelAdmin(UserAdmin):
    ...

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    ...

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...
