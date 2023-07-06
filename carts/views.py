from .serializers import CartSerializer
from .models import Cart
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .permissions import IsCartOwner
from products.models import Product


# Create your views here.
class CartView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser | IsCartOwner]
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def perform_create(self, serializer):
        product = Product.objects.get(id=self.kwargs["pk"])
        quantity = self.request.data["quantity"]
        serializer.save(user=self.request.user, product=product, quantity=quantity)
