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
        labels = {label: "" for label in fields}
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
                attrs={"class": "form-control", "placeholder": "ip-адрес"}
            ),
        }

    def clean(self):
        cleaned_data = super().clean()
        inv_num = cleaned_data.get("inv_num")
        serial = cleaned_data.get("serial")

        if Device.objects.filter(inv_num=inv_num).exists():
            self.add_error(
                "inv_num", "Устройство с таким инвентарным номером уже существует"
            )

        if Device.objects.filter(serial=serial).exists():
            self.add_error(
                "serial", "Устройство с таким серийным номером уже существует"
            )

        return cleaned_data
