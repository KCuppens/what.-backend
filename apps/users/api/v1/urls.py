from django.urls import path

from .viewsets import LoginView


urlpatterns = [
    path("login-user/", LoginView.as_view(), name="login-user"),
]
