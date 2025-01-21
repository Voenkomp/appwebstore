from django.shortcuts import render
from .forms import DeviceForm


def addprinter(request):
    error = ""
    if request.method == "POST":
        form = DeviceForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = "Форма была неверной"
    form = DeviceForm()
    data = {"form": form, "error": error}
    return render(request, "adddevice/addprinter.html", data)
