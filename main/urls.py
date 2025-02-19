from django.urls import path
from . import views
from adddevice.views import DeviceUpdateView

urlpatterns = [
    path("", views.index, name="home"),
    path("all/", views.all_devices, name="all-devices"),
    path("about/", views.about, name="about"),
    path("device/<int:pk>", views.DeviceDetailView.as_view(), name="device-detail"),
    path("device/<int:pk>/update", DeviceUpdateView.as_view(), name="device-update"),
    path(
        "device/<int:pk>/delete", views.DeviceDeleteView.as_view(), name="device-delete"
    ),
]
