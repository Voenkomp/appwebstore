from django.shortcuts import render
from django.http import HttpResponse
from adddevice.models import Device
from django.views.generic import DetailView


def index(request):
    device = Device.objects.order_by("inv_num")
    return render(request, "main/index.html", {"device": device})


class DeviceDetailView(DetailView):
    model = Device
    template_name = "main/detail_device.html"
    context_object_name = "printer"


def about(request):
    return render(request, "main/about.html")
