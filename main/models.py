from django.db import models


class ProducerModel(models.Model):
    producer_model = models.CharField(
        "Производитель и модель", max_length=50, unique=True
    )
    create_time = models.DateTimeField("Время создания", auto_now_add=True)

    def __str__(self):
        return f"{self.producer_model}"

    class Meta:
        verbose_name = "Принтер"
        verbose_name_plural = "Принтеры"


class Cartridges(models.Model):
    prod_mod = models.ManyToManyField(
        ProducerModel, verbose_name="Модель", related_name="model"
    )
    cartridge = models.CharField("Картридж", max_length=50, unique=True)
    create_time = models.DateTimeField("Время создания", auto_now_add=True)

    def __str__(self):
        return f"{self.cartridge}"

    class Meta:
        verbose_name = "Картридж"
        verbose_name_plural = "Картриджи"


class Device(models.Model):
    inv_num = models.CharField("Инвентарный номер", max_length=15)
    serial = models.CharField("Серийный номер", max_length=20, blank=True)
    prod_mod_dev = models.ForeignKey(
        ProducerModel,
        on_delete=models.CASCADE,
        verbose_name="Модель",
        related_name="producermodelset",
    )
    building = models.CharField("Корпус", max_length=10)
    location = models.CharField("Расположение", max_length=50)
    note = models.CharField("Примечание", max_length=250, blank=True)
    hostname = models.CharField("Hostname", max_length=30, blank=True)
    ip_add = models.CharField("ip-адрес", max_length=30, blank=True)

    def __str__(self):
        return f"{self.inv_num} {self.prod_mod_dev} {self.building} {self.location}"

    def get_absolute_url(self):
        return f"/device/{self.id}"

    class Meta:
        verbose_name = "Устройство"
        verbose_name_plural = "Устройства"
