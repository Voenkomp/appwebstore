from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Device, Cartridges, UserSettings
from django.views.generic import DetailView, UpdateView, DeleteView
from .filters import DeviceFilter
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from .forms import UserSettingsForm


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
    note_check = request.user.usersettings.note_filter
    if not request.GET:
        try:
            settings = UserSettings.objects.get(user=request.user)
            initial_data = {}
            if settings.default_building:
                initial_data["building"] = settings.default_building
        except UserSettings.DoesNotExist:
            initial_data = {}
        filter = DeviceFilter(
            data=initial_data, queryset=devices, note_check=note_check, request=request
        )
    else:
        filter = DeviceFilter(
            data=request.GET, queryset=devices, note_check=note_check, request=request
        )
    return render(
        request, "main/all_devices.html", {"devices": filter, "note_check": note_check}
    )


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


@login_required
def settings(request):
    settings, created = UserSettings.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = UserSettingsForm(request.POST, instance=settings)
        if form.is_valid():
            form.save()
            return redirect("settings")
    else:
        form = UserSettingsForm(instance=settings)
    return render(request, "main/settings.html", {"form": form})


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


@login_required
def about(request):
    return render(request, "main/about.html")


@login_required
def whatsnew(request):
    return render(request, "main/whatsnew.html")
