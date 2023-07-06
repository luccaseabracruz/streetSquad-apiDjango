from django.urls import path
from . import views
from .views import RequestView, RequestDetailsView

urlpatterns = [
    path("users/requests/", views.RequestView.as_view()),
    path("requests/<int:pk>/", views.RequestDetailsView.as_view())
]
