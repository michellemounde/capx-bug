from django.urls import path

from . import views

app_name = "bug"
urlpatterns = [
    # ex: /bug/
    path("", views.index, name="index"),
    # ex: /bug/register/
    path("register/", views.register_bug, name="register"),
    # ex: /bug/bugs/
    path("bugs/", views.BugsView.as_view(), name="bugs"),
    # ex: /bug/1/
    path("<int:pk>/", views.DetailView.as_view(), name="detail")
]
