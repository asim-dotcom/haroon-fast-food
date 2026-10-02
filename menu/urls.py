
from django.urls import path
from . import views


urlpatterns = [
    path("", views.menu_list, name="menu_list"),
    path("checkout/", views.checkout, name="checkout"),
    path(
        "order/<uuid:reference>/",
        views.order_confirmation,
        name="order_confirmation",
    ),
]