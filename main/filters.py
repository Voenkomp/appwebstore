import django_filters
from django.forms import TextInput, CheckboxSelectMultiple, SelectMultiple, Select
from .models import Device, UserSettings


class DeviceFilter(django_filters.FilterSet):

    inv_num = django_filters.CharFilter(
        field_name="inv_num",
        lookup_expr="icontains",
        label="",
        widget=TextInput(
            attrs={
                "class": "form-control form-filter custom-form-filter",
                "placeholder": "Инвентарный номер",
            }
        ),
    )

    serial = django_filters.CharFilter(
        lookup_expr="icontains",
        label="",
        widget=TextInput(
            attrs={
                "class": "form-control form-filter custom-form-filter",
                "placeholder": "Серийный номер",
            }
        ),
    )

    prod_mod_dev = django_filters.CharFilter(
        field_name="prod_mod_dev__producer_model",
        lookup_expr="icontains",
        label="",
        widget=TextInput(
            attrs={
                "class": "form-control form-filter custom-form-filter",
                "placeholder": "Модель",
            }
        ),
    )

    building = django_filters.MultipleChoiceFilter(
        field_name="building",
        lookup_expr="iexact",
        label="",
        widget=CheckboxSelectMultiple(attrs={"class": "form-check-input"}),
        choices=[],
    )

    location = django_filters.CharFilter(
        lookup_expr="icontains",
        label="",
        widget=TextInput(
            attrs={
                "class": "form-control form-filter custom-form-filter",
                "placeholder": "Расположение",
            }
        ),
    )

    hostname = django_filters.CharFilter(
        lookup_expr="icontains",
        label="",
        widget=TextInput(
            attrs={
                "class": "form-control form-filter custom-form-filter",
                "placeholder": "Hostname",
            }
        ),
    )

    ip_add = django_filters.CharFilter(
        lookup_expr="icontains",
        label="",
        widget=TextInput(
            attrs={
                "class": "form-control form-filter custom-form-filter",
                "placeholder": "IP-адрес",
            }
        ),
    )

    class Meta:
        model = Device
        fields = ["building"]

    def __init__(self, data=None, queryset=None, request=None, *args, **kwargs):

        self.note_check = kwargs.pop("note_check", None)
        super().__init__(data, queryset, request=request, *args, **kwargs)
        if self.note_check:
            self.filters["note"] = django_filters.CharFilter(
                field_name="note",
                lookup_expr="icontains",
                label="",
                widget=TextInput(
                    attrs={
                        "class": "form-control form-filter custom-form-filter",
                        "placeholder": "Примечание",
                    }
                ),
            )

        buildings = Device.objects.values_list("building", flat=True).distinct()
        self.filters["building"].extra["choices"] = [(b, b) for b in buildings]

        if request and not data:
            try:
                settings = UserSettings.objects.get(user=request.user)
                if settings.default_building:
                    self.form.fields["building"].initial = settings.default_building
            except UserSettings.DoesNotExist:
                pass
