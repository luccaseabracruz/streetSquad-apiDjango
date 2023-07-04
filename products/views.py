from .serializers import ProductSerializer
from .models import Product
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser
from .permissions import IsSellerOrReadOnly, IsAdminOrSellerOwner


class ProductView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSellerOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrSellerOwner]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
