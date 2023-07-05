from django.urls import path
from . import views
from .views import RequestView, RequestDetailsView, RequestsBybuier

urlpatterns = [
    path("users/requests/", views.RequestView.as_view()),
    path("products/<int:product_id>/requests/", views.RequestDetailsView.as_view()),
    path("users/orders/", views.RequestsBybuier.as_view()),
]
