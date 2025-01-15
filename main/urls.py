from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("add/", views.addprinter, name="addprinter"),
    path("about/", views.about, name="about"),
]
