from django.contrib import admin
from .models import ProducerModel, Cartridges, Device

# Register your models here.

admin.site.register(ProducerModel)
admin.site.register(Cartridges)
admin.site.register(Device)
