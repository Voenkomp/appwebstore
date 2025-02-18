from django.shortcuts import render
from django.http import JsonResponse
from .models import Device, Cartridges, ProducerModel
from adddevice.forms import DeviceForm
from django.views.generic import DetailView, UpdateView, DeleteView
from .filters import DeviceFilter
from dal import autocomplete


def index(request):
    device = Device.objects.order_by("id")
    return render(request, "main/index.html", {"device": device})


def all_devices(request):
    devices = Device.objects.prefetch_related("prod_mod_dev__model").all()
    filter = DeviceFilter(request.GET, queryset=devices)
    return render(request, "main/all_devices.html", {"devices": filter})


class DeviceDetailView(DetailView):
    model = Device
    template_name = "main/detail_device.html"
    context_object_name = "printer"


class DeviceDeleteView(DeleteView):
    model = Device
    success_url = "/"
    template_name = "adddevice/deleteprinter.html"


# class ProducerModelAutocomlete(autocomplete.Select2QuerySetView):
#     def get_queryset(self):
#         qs = ProducerModel.objects.all()
#         if self.q:
#             qs = qs.filter(name__icontains=self.q)
#         return qs


def about(request):
    return render(request, "main/about.html")
