from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Device, Cartridges
from django.views.generic import DetailView, UpdateView, DeleteView
from .filters import DeviceFilter
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect


class CustomLoginView(LoginView):
    template_name = "main/registration.html"
    redirect_authenticated_user = True


class CustomLogoutView(LogoutView):
    next_page = "login"


@login_required
def index(request):
    # favorite_devices = request.user.favorite_devices.all()
    favorite_devices = request.user.favorite_devices.all()
    return render(request, "main/index.html", {"devices": favorite_devices})


@login_required
def all_devices(request):
    devices = Device.objects.prefetch_related("prod_mod_dev__model").all()
    filter = DeviceFilter(request.GET, queryset=devices)
    return render(request, "main/all_devices.html", {"devices": filter})


@login_required
def toggle_favorite(request, pk):
    device = get_object_or_404(Device, id=pk)

    if request.user in device.favorite_users.all():
        device.favorite_users.remove(request.user)
    else:
        device.favorite_users.add(request.user)

    return redirect(request.META.get("HTTP_REFERER", "home"))


@login_required
def update_descr(request, pk):
    device = get_object_or_404(Device, pk=pk)

    if request.method == "POST":
        device.description = request.POST.get("description", "").strip()
        device.save()

        return redirect("device-detail", pk=device.pk)

    # return redirect("device_detail", pk=device.pk)


class DeviceDetailView(LoginRequiredMixin, DetailView):
    model = Device
    template_name = "main/detail_device.html"
    context_object_name = "device"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        device = self.object
        producer_model = device.prod_mod_dev
        cartridges = Cartridges.objects.filter(prod_mod=producer_model)
        context["cartridges"] = cartridges
        return context


class DeviceDeleteView(LoginRequiredMixin, DeleteView):
    model = Device
    success_url = "/"
    template_name = "adddevice/deleteprinter.html"


# class ProducerModelAutocomlete(autocomplete.Select2QuerySetView):
#     def get_queryset(self):
#         qs = ProducerModel.objects.all()
#         if self.q:
#             qs = qs.filter(name__icontains=self.q)
#         return qs


@login_required
def about(request):
    return render(request, "main/about.html")
