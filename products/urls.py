from django.urls import path
from products import views


urlpatterns = [
    path("products/", views.ProductView.as_view()),
    path("products/", views.CreateProductView.as_view()),
    path("products/<int:product_id>", views.ProductDetailView.as_view())
]