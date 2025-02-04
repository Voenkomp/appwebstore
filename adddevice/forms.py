from main.models import Device, ProducerModel
from django.forms import ModelForm, TextInput, ModelChoiceField, Select
from dal import autocomplete


class DeviceForm(ModelForm):
    prod_mod_dev = ModelChoiceField(
        queryset=ProducerModel.objects.all(),
        widget=autocomplete.ModelSelect2(url="device-autocomplete"),
        required=False,
        label="Выберите принтер",
    )

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
                attrs={"class": "form-control", "placeholder": "ip-адрес"}
            ),
        }
