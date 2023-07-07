from django.shortcuts import render
from .models import Address
from .serializers import AddressSerializer
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser
from users.permissions import IsAccountOwnerOrAdmin
from .permissions import IsAddressOwnerOrAdmin
from django.shortcuts import get_object_or_404
from users.models import User
from django.db.utils import IntegrityError
from rest_framework.views import Response, status


class CreateAddressView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwnerOrAdmin]
    serializer_class = AddressSerializer
    queryset = Address.objects.all()

    def perform_create(self, serializer):
        selected_user = get_object_or_404(User, pk=self.kwargs.get('pk'))
        self.check_object_permissions(self.request, selected_user)
        serializer.save(user=selected_user)


class AddressDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAddressOwnerOrAdmin]
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def get_object(self):
        user = get_object_or_404(User, pk=self.kwargs.get('pk'))
        address = get_object_or_404(Address, user=user)
        self.check_object_permissions(self.request, address)
        return address
