from rest_framework import permissions
from .models import Cart
from rest_framework.views import View, Request


class IsCartOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: Cart) -> bool:
        return obj == request.user or obj.cart.user == request.user
