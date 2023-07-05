from rest_framework import permissions
from .models import Request as Order
from rest_framework.views import View, Request


class IsOrderOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: Order):
        if request.user.is_superuser:
            return True
        return (
            request.user.is_authenticated
            and obj.buyer == request.user
        )
