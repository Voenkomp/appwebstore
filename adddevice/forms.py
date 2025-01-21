from .models import Device
from django.forms import ModelForm, TextInput


class DeviceForm(ModelForm):
    class Meta:
        model = Device
        fields = [
            "inv_num",
            "producer",
            "model",
            "serial",
            "cartridge",
            "building",
            "location",
            "note",
            "net_address",
        ]
        widgets = {
            "inv_num": TextInput(
                attrs={"class": "form-control", "placeholder": "Инвентарный номер"}
            ),
            "producer": TextInput(
                attrs={"class": "form-control", "placeholder": "Производитель"}
            ),
            "model": TextInput(
                attrs={"class": "form-control", "placeholder": "Модель"}
            ),
            "serial": TextInput(
                attrs={"class": "form-control", "placeholder": "Серийный номер"}
            ),
            "cartridge": TextInput(
                attrs={"class": "form-control", "placeholder": "Картридж"}
            ),
            "building": TextInput(
                attrs={"class": "form-control", "placeholder": "Корпус"}
            ),
            "location": TextInput(
                attrs={"class": "form-control", "placeholder": "Расположение"}
            ),
            "note": TextInput(
                attrs={"class": "form-control", "placeholder": "Примечание"}
            ),
            "net_address": TextInput(
                attrs={"class": "form-control", "placeholder": "Hostname/IP"}
            ),
        }
