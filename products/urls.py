from django.urls import path
from products import views
from carts.views import CartView, CartListView


urlpatterns = [
    path("products/", views.ProductView.as_view()),
    path("products/<int:pk>/", views.ProductDetailView.as_view()),
    path("products/<int:pk>/add/", CartView.as_view()),
    path("user/cart/", CartListView.as_view())
]