from django.urls import path
from . import views

urlpatterns = [
    path("", views.DeviceCreateView.as_view(), name="addprinter"),
    path(
        "device/<int:pk>/update", views.DeviceUpdateView.as_view(), name="device-update"
    ),
    path(
        "device-autocomplete/",
        views.ProducerModelAutocomlete.as_view(),
        name="device-autocomplete",
    ),
]
