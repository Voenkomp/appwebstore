from django.db import models


class Device(models.Model):
    inv_num = models.CharField("Инвентарный номер", max_length=15)
    producer = models.CharField("Производитель", max_length=20)
    model = models.CharField("Модель", max_length=35)
    serial = models.CharField("Серийный номер", max_length=20, null=True)
    cartridge = models.CharField("Картридж", max_length=15)
    building = models.CharField("Корпус", max_length=5)
    location = models.CharField("Расположение", max_length=10)
    note = models.CharField("Примечание", max_length=250)
    net_address = models.CharField("Hostname/IP", max_length=30)

    def __str__(self):
        return self.inv_num

    def get_absolute_url(self):
        return f"/device/{self.id}"

    class Meta:
        verbose_name = "Устройство"
        verbose_name_plural = "Устройства"
