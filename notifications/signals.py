from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserNotification


@receiver(post_save, sender=UserNotification)
def log_user_notification_creation(sender, instance, created, **kwargs):
    if created:
        print(f"[SIGNAL] A new UserNotification was created: {instance}")
