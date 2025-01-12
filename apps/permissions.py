from rest_framework import permissions


class IsCourier(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.type=='courier':
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser or obj.courier==request.user:
            return True
        return False