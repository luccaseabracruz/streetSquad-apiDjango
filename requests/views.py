from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .serializers import RequestSerializer
from .models import Request
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication


class RequestView(generics.ListCreateAPIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'user_id'
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.kwargs.get("user_id"))


class RequestDetailsView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Request.objects.all()
    serializer_class = RequestSerializer


class RequestBySeller(generics.ListAPIView):
    ...
