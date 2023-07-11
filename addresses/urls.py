from django.urls import path
from addresses import views as addresses_views


urlpatterns = [
    path(
        "users/<int:pk>/addresses/create/", addresses_views.CreateAddressView.as_view()
    ),
    path("users/<int:pk>/addresses/", addresses_views.AddressDetailView.as_view()),
]
