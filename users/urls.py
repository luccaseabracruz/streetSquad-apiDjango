from django.urls import path
from users import views as users_views
from addresses import views as addresses_views
from rest_framework_simplejwt import views as jwt_views
from products import views as products_views
from order_requests.views import RequestBySeller, RequestsBybuier
from carts.views import CartListView, CartRetrieveUpdateDestroyView


urlpatterns = [
    path("users/", users_views.CreateUserView.as_view()),
    path("users/list/", users_views.ListUsersView.as_view()),
    path("users/login/", jwt_views.TokenObtainPairView.as_view()),
    path("users/<int:pk>/", users_views.UserDetailView.as_view()),
    path(
        "users/<int:pk>/addresses/create/",
        addresses_views.CreateAddressView.as_view()
    ),
    path(
        "users/<int:pk>/addresses/",
        addresses_views.AddressDetailView.as_view()
    ),
    path(
        "users/products/",
        products_views.ProductBySeller.as_view()
    ),
    path(
        "users/orders/",
        RequestsBybuier.as_view()
    ),
    path(
        "users/sales/",
        RequestBySeller.as_view()
    ),
    path("users/mycart/", CartListView.as_view()),
    path("users/mycart/<int:pk>/", CartRetrieveUpdateDestroyView.as_view())
]
