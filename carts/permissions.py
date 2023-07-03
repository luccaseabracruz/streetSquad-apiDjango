from rest_framework import permissions
from .models import Cart
from rest_framework.views import View


class IsCartOwner(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: Cart) -> bool:
        return request.user.is_authenticated and obj == request.user