from rest_framework import generics
from .serializers import RequestSerializer
from .models import Request
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication


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
