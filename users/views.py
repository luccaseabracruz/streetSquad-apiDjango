from django.shortcuts import render
from .models import User
from .serializers import UserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import CreateAPIView, ListAPIView,RetrieveUpdateDestroyAPIView 
from rest_framework.permissions import IsAdminUser
from .permissions import IsAccountOwnerOrAdmin


class CreateUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = [UserSerializer]

class ListUsersView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = [UserSerializer]


class UserDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwnerOrAdmin]
    queryset = User.objects.all()
    serializer_class = [UserSerializer]
