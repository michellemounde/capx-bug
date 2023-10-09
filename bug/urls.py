from django.urls import path

from . import views

urlpatterns = [
    # ex: /bug/
    path("", views.index, name="index"),
    # ex: /bug/register/
    path("register", views.register_bug, name="register")
]
