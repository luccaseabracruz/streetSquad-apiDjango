from rest_framework import permissions
from .models import Address
from rest_framework.views import View, Request
from rest_framework import permissions


class IsAddressOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: Address):
        if (request.user.is_authenticated and request.method in permissions.SAFE_METHODS):
            if request.user.is_seller or obj.user == request.user:
                return True
            if request.user.is_superuser:
                return True
            return False
        
        return (
            request.user.is_superuser
            or obj.user == request.user
        )
