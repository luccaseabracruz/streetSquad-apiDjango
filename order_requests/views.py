from rest_framework import generics
from .serializers import RequestSerializer
from .models import Request
from users.models import User
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from products.permissions import IsSellerOwnerOrAdmin
from .permissions import IsOrderOwnerOrAdmin


class RequestView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
   
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    
    def perform_create(self, serializer):
        serializer.save(buyer=self.request.user)

class RequestDetailsView(generics.RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOrderOwnerOrAdmin]
    
    queryset = Request.objects.all()
    serializer_class = RequestSerializer


class RequestBySeller(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSellerOwnerOrAdmin]
    serializer_class = RequestSerializer

    def get_queryset(self):
        return Request.objects.filter(seller=self.request.user.id)


class RequestsBybuier(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = RequestSerializer

    def get_queryset(self):
        return Request.objects.filter(buyer_id=self.request.user.id)