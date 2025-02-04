from django.shortcuts import render
from .forms import DeviceForm
from dal import autocomplete
from django.http import JsonResponse
from main.views import ProducerModel


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


class ProducerModelAutocomlete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = ProducerModel.objects.all()
        if self.q:
            qs = qs.filter(producer_model__icontains=self.q)
        return qs
