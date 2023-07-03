from django.shortcuts import render
from .models import Address
from .serializers import AddressSerializer
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser
from users.permissions import IsAccountOwner
from .permissions import IsAddressOwner


class CreateAddressView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser | IsAccountOwner]
    serializer_class = AddressSerializer
    queryset = Address.objects.all()

    def perform_create(self, serializer):
        serializer.save(user_id=self.kwargs.get(self.lookup_field))


class AddressDetailView(generics.RetrieveUpdateDestroyAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser | IsAddressOwner]
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def get_queryset(self):
        return Address.objects.filter(
            user_id=self.kwargs.get(self.lookup_field)
        )
