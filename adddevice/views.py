from django.shortcuts import render, redirect
from .forms import DeviceForm
from dal import autocomplete
from django.http import JsonResponse
from main.views import ProducerModel
from django.contrib import messages


def addprinter(request):
    if request.method == "POST":
        form = DeviceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Устройство успешно добавлено")
            return redirect("/add")
        else:
            messages.error(request, "Ошибка. Проверьте форму")
    else:
        form = DeviceForm()
    data = {"form": form}
    return render(request, "adddevice/addprinter.html", data)


class ProducerModelAutocomlete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = ProducerModel.objects.all()
        if self.q:
            qs = qs.filter(producer_model__icontains=self.q)
        return qs
