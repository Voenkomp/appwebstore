from django.contrib import admin
from .models import ProducerModel, Cartridges, Device


# Register your models here.

# admin.site.register(ProducerModel)
# admin.site.register(Cartridges)
# admin.site.register(Device)


@admin.register(ProducerModel)  # этот декоратор аналог метода admin.site.register()
class ProducerModelAdmin(admin.ModelAdmin):
    search_fields = ["producer_model"]


@admin.register(Cartridges)
class CartridgesAdmin(admin.ModelAdmin):
    autocomplete_fields = ["prod_mod"]


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    autocomplete_fields = ["prod_mod_dev"]
