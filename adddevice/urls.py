from django.urls import path
from . import views

urlpatterns = [
    path("", views.addprinter, name="addprinter"),
    path(
        "device-autocomplete/",
        views.ProducerModelAutocomlete.as_view(),
        name="device-autocomplete",
    ),
]
