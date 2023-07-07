from .serializers import CartProductsSerializer
from .models import Cart, CartProducts
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .permissions import IsCartOwner
from django.forms.models import model_to_dict


# Create your views here.
class CartView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser | IsCartOwner]
    queryset = Cart.objects.all()
    serializer_class = CartProductsSerializer


class CartListView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser | IsCartOwner]
    queryset = Cart.objects.all()
    serializer_class = CartProductsSerializer

    def get_queryset(self):
        cart = Cart.objects.get(user=self.request.user)
        return CartProducts.objects.filter(cart=cart)


class CartRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsCartOwner]
    queryset = CartProducts.objects.all()
    serializer_class = CartProductsSerializer
