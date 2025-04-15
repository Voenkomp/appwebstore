import django_filters
from django.forms import TextInput


class DeviceFilter(django_filters.FilterSet):
    inv_num = django_filters.CharFilter(
        field_name="inv_num",
        lookup_expr="icontains",
        label="",
        widget=TextInput(
            attrs={
                "class": "form-control form-filter",
                "placeholder": "Инвентарный номер",
            }
        ),
    )

    serial = django_filters.CharFilter(
        lookup_expr="icontains",
        label="",
        widget=TextInput(
            attrs={"class": "form-control form-filter", "placeholder": "Серийный номер"}
        ),
    )

    prod_mod_dev = django_filters.CharFilter(
        field_name="prod_mod_dev__producer_model",
        lookup_expr="icontains",
        label="",
        widget=TextInput(
            attrs={"class": "form-control form-filter", "placeholder": "Модель"}
        ),
    )

    building = django_filters.CharFilter(
        lookup_expr="icontains",
        label="",
        widget=TextInput(
            attrs={"class": "form-control form-filter", "placeholder": "Здание"}
        ),
    )

    location = django_filters.CharFilter(
        lookup_expr="icontains",
        label="",
        widget=TextInput(
            attrs={"class": "form-control form-filter", "placeholder": "Расположение"}
        ),
    )

    hostname = django_filters.CharFilter(
        lookup_expr="icontains",
        label="",
        widget=TextInput(
            attrs={"class": "form-control form-filter", "placeholder": "Hostname"}
        ),
    )

    ip_add = django_filters.CharFilter(
        lookup_expr="icontains",
        label="",
        widget=TextInput(
            attrs={"class": "form-control form-filter", "placeholder": "IP-адрес"}
        ),
    )
