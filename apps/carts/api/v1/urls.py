from django.urls import path

from .viewsets import ToggleCartItemView


urlpatterns = [
    path("toggle-cart-item/", ToggleCartItemView.as_view(), name="toggle-cart-item"),
]
