from rest_framework import permissions
from .models import Address
from rest_framework.views import View, Request


class IsAddressOwner(permissions.BasePermission):
    def has_object_permission(self, request, View, obj):
        return (
            request.user.is_seller
            or request.user.address == obj
        )
