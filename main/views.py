from django.shortcuts import render
from django.http import HttpResponse
from adddevice.models import Device
from adddevice.forms import DeviceForm
from django.views.generic import DetailView, UpdateView, DeleteView


def index(request):
    device = Device.objects.order_by("inv_num")
    return render(request, "main/index.html", {"device": device})


def all_devices(request):
    device = Device.objects.order_by("inv_num")
    return render(request, "main/all_devices.html", {"device": device})


class DeviceDetailView(DetailView):
    model = Device
    template_name = "main/detail_device.html"
    context_object_name = "printer"


class DeviceUpdateView(UpdateView):
    model = Device
    template_name = "adddevice/addprinter.html"
    form_class = DeviceForm


class DeviceDeleteView(DeleteView):
    model = Device
    success_url = "/"
    template_name = "adddevice/deleteprinter.html"


def about(request):
    return render(request, "main/about.html")
