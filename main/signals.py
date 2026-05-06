from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserSettings


@receiver(post_save, sender=User)
def create_user_settings(sender, instance, created, **kwargs):
    """Создаёт настройки для нового пользователя"""
    if created:
        UserSettings.objects.create(user=instance)
        print(f"Созданы настройки для пользователя {instance.username}")  # для отладки


@receiver(post_save, sender=User)
def save_user_settings(sender, instance, **kwargs):
    """Сохраняет настройки пользователя (нужно для админки)"""
    # Проверяем, существует ли уже объект настроек
    if hasattr(instance, "settings"):
        instance.usersettings.save()
