from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("about/", views.about, name="about"),
    path("device/<int:pk>", views.DeviceDetailView.as_view(), name="device-detail"),
]
