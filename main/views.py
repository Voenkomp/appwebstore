from django.shortcuts import render
from django.http import HttpResponse
from adddevice.models import Device


def index(request):
    device = Device.objects.order_by("inv_num")
    return render(request, "main/index.html", {"device": device})


def about(request):
    return render(request, "main/about.html")
