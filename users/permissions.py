from rest_framework import permissions
from .models import User
from rest_framework.views import View, Request


class IsAccountOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request: Request, View, obj: User):
        if request.user.is_superuser:
            return True
        return (
            request.user.is_authenticated
            and obj == request.user
        )
