from django.urls import path
from users import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("users/", views.CreateUserView.as_view()),
    path("users/", views.ListUsersView.as_view()),
    path("users/<int:pk>", views.UserDetailView.as_view()),
    path("users/login", jwt_views.TokenObtainPairView.as_view()),
]
