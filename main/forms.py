from django import forms
from .models import UserSettings
from .models import Device


class UserSettingsForm(forms.ModelForm):
    default_building = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Здания в которых будет поиск по умолчанию",
    )
    note_filter = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"}),
        label='Добавить строку "Примечание" на странице Все устройства:',
    )

    class Meta:
        model = UserSettings
        fields = ["note_filter", "default_building"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        buildings = Device.objects.values_list("building", flat=True).distinct()
        self.fields["default_building"].choices = [(b, b) for b in buildings]

        if self.instance and self.instance.default_building:
            self.initial["default_building"] = self.instance.default_building
        if self.instance:
            self.initial["note_filter"] = self.instance.note_filter

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.default_building = self.cleaned_data["default_building"]
        instance.note_filter = self.cleaned_data["note_filter"]
        if commit:
            instance.save()
        return instance
