from rest_framework import generics
from .serializers import RequestSerializer
from .models import Request
from users.models import User
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from products.permissions import IsSellerOwnerOrAdmin


class RequestView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
   
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    
    def perform_create(self, serializer):
        serializer.save(buyer=self.request.user)

class RequestDetailsView(generics.RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    queryset = Request.objects.all()
    serializer_class = RequestSerializer


class RequestBySeller(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSellerOwnerOrAdmin]
    serializer_class = RequestSerializer

    def get_queryset(self):
        return Request.objects.filter(product__user=self.request.user)


class RequestsBybuier(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = RequestSerializer

    def get_queryset(self):
        return Request.objects.filter(buyer=self.request.user)