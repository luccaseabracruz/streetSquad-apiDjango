from django.urls import path
from . import views
from .views import RequestView, RequestDetailsView

urlpatterns = [
    path("users/<int:user_id>/requests/", views.RequestView.as_view()),
    path("products/<int:product_id>/requests/", views.RequestDetailsView.as_view())
]
