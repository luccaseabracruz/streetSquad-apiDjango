from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from products.models import Product
from .serializers import RequestSerializer
from .models import Request
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication


class RequestView(generics.ListCreateAPIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
   
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

    def perform_create(self, serializer):
        product_id = self.request.data.get('product')
        serializer.save(buyer=self.request.user, product=product_id)
        stock_quantity = Product.objects.filter(id=1)
        print(stock_quantity)


class RequestDetailsView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = "product_id"

    queryset = Request.objects.all()
    serializer_class = RequestSerializer
