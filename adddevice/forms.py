from main.models import Device, ProducerModel
from django.forms import ModelForm, TextInput, ModelChoiceField, Select
from dal import autocomplete


class DeviceForm(ModelForm):

    class Meta:
        model = Device
        fields = [
            "inv_num",
            "serial",
            "prod_mod_dev",
            "building",
            "location",
            "note",
            "hostname",
            "ip_add",
        ]
        # labels = {label: "" for label in fields}
        widgets = {
            "inv_num": TextInput(
                attrs={"class": "form-control", "placeholder": "Инвентарный номер"}
            ),
            "serial": TextInput(
                attrs={"class": "form-control", "placeholder": "Серийный номер"}
            ),
            "prod_mod_dev": autocomplete.ModelSelect2(
                url="device-autocomplete",
                attrs={
                    "class": "form-control",
                    "data-placeholder": "Выберите устройство",
                    "data-theme": "bootstrap-5",
                },
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
            "hostname": TextInput(
                attrs={"class": "form-control", "placeholder": "Hostname"}
            ),
            "ip_add": TextInput(
                attrs={"class": "form-control", "placeholder": "IP-адрес"}
            ),
        }
