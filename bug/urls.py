from django.urls import path

from . import views

app_name = "bug"
urlpatterns = [
    # ex: /bug/
    path("", views.index, name="index"),
    # ex: /bug/register/
    path("register/", views.register_bug, name="register"),
    # ex: /bug/bugs/
    path("bugs/", views.bugs, name="bugs"),
    # ex: /bug/1/
    path("<int:bug_id>/", views.detail, name="detail")
]
