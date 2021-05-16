from django.urls import path

from . import views

urlpatterns = [
path("<int:id>", views.index, name="index"),
path("start/", views.index2, name="start"),
path("", views.home, name="home"),
]
