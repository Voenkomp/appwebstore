import django_filters
from .models import Device
from django.forms import ModelForm, TextInput


class DeviceFilter(django_filters.FilterSet):
    inv_num = django_filters.CharFilter(
        lookup_expr="icontains",
        label="Инвентарный номер",
    )

    class Meta:
        model = Device
        fields = ["inv_num"]
