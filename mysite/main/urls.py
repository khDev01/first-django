from django.urls import path

from . import views

urlpatterns = [
path("", views.index, name="index"),
path("start/", views.index2, name="start"),
]
