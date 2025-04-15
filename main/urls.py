from django.urls import path
from . import views
from adddevice.views import DeviceUpdateView
from django.contrib.auth import views as auth_views
from .views import CustomLoginView, CustomLogoutView

urlpatterns = [
    path("", views.index, name="home"),
    path("all/", views.all_devices, name="all-devices"),
    path("about/", views.about, name="about"),
    path("device/<int:pk>", views.DeviceDetailView.as_view(), name="device-detail"),
    path("device/<int:pk>/update", DeviceUpdateView.as_view(), name="device-update"),
    path(
        "device/<int:pk>/delete", views.DeviceDeleteView.as_view(), name="device-delete"
    ),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path(
        "device/<int:pk>/toggle_favorite/",
        views.toggle_favorite,
        name="toggle_favorite",
    ),
    path("device/<int:pk>/update_descr", views.update_descr, name="update-descr"),
]
