from django.shortcuts import render, redirect
from .forms import DeviceForm
from django.urls import reverse_lazy
from dal import autocomplete
from main.views import ProducerModel
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
            messages.error(
                self.request,
                f"Устройство {inv_num} уже существует",
                extra_tags="error_inv_num",
            )
            # return self.form_invalid(form)
        elif Device.objects.filter(serial=serial).exists():
            messages.error(
                self.request,
                f"Устройство {serial} уже существует",
                extra_tags="error_serial",
            )
            # return self.form_invalid(form)
        if messages.error:
            return self.form_invalid(form)
        messages.success(self.request, "Устройство успешно добавлено!")
        return super().form_valid(form)

    # def form_invalid(self, form):
    #     # Добавляем сообщения об ошибках вручную
    #     for field, errors in form.errors.items():
    #         for error in errors:
    #             messages.error(self.request, f"{form.fields[field].label}: {error}")
    #     return super().form_invalid(form)


class DeviceUpdateView(UpdateView):
    model = Device
    template_name = "adddevice/device_update_form.html"
    form_class = DeviceForm


class ProducerModelAutocomlete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = ProducerModel.objects.all()
        if self.q:
            qs = qs.filter(producer_model__icontains=self.q)
        return qs
