from apps.models.users import User


class UserAdmin(User):
    class Meta:
        proxy = True
        verbose_name = 'Admin User'
        verbose_name_plural = 'Admin Users'

class UserCourier(User):
    class Meta:
        proxy = True
        verbose_name = 'Courier User'
        verbose_name_plural = 'Courier Users'
