from django.shortcuts import render, redirect
from .forms import DeviceForm
from django.urls import reverse_lazy, reverse
from dal import autocomplete
from main.models import ProducerModel
from django.contrib import messages
from django.views.generic import CreateView, UpdateView
from main.models import Device


class DeviceCreateView(CreateView):
    model = Device
    form_class = DeviceForm
    template_name = "adddevice/addprinter.html"
    success_url = reverse_lazy("addprinter")

    def form_valid(self, form):
        inv_num = form.cleaned_data.get("inv_num")
        serial = form.cleaned_data.get("serial")
        if Device.objects.filter(inv_num=inv_num).exists():
            form.add_error("inv_num", f"Устройство {inv_num} уже существует")
        if Device.objects.filter(serial=serial).exists():
            form.add_error("serial", f"Устройство с {serial} уже существует")
        if form.errors:
            return self.form_invalid(form)
        messages.success(self.request, "Устройство успешно добавлено!")
        return super().form_valid(form)


class DeviceUpdateView(UpdateView):
    model = Device
    form_class = DeviceForm
    template_name = "adddevice/device_update_form.html"
    # success_url = reverse_lazy("device-update")

    def get_success_url(self):
        return reverse("device-update", kwargs={"pk": self.object.pk})

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["inv_num"].disabled = True
        form.fields["serial"].disabled = True
        return form

    def form_valid(self, form):
        messages.success(self.request, "Устройство обновлено")
        return super().form_valid(form)


class ProducerModelAutocomlete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = ProducerModel.objects.all()
        if self.q:
            qs = qs.filter(producer_model__icontains=self.q)
        return qs
