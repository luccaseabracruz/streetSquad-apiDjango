from django.urls import path
from . import views
from .views import RequestView, RequestDetailsView, RequestsBybuier

urlpatterns = [
    path("users/requests/", views.RequestView.as_view()),
    path("requests/<int:pk>/", views.RequestDetailsView.as_view()),
    path("requests/all/", views.RequestAllView.as_view()),
]
