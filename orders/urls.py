from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("menu/", views.menu, name="menu"),
    path("menu/<str:category>/", views.submenu, name="submenu"),
    path("cart", views.cart, name="cart"),
    path("register", views.register, name="register")
]
