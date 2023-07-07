from rest_framework import permissions
from rest_framework.views import Request, View
from users.models import User


class IsSellerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view: View) -> bool:
        return bool(
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
            and request.user.is_seller
        )


class IsAdminOrSellerOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj) -> bool:
        return bool(
            request.method in permissions.SAFE_METHODS
            or request.user.is_superuser
            or obj.user == request.user
        )


class IsSellerOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj) -> bool:
        return request.user.is_superuser or obj.user == request.user
