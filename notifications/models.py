from django.db import models


class UserNotification(models.Model):
    name = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=100, null=True)
    message = models.TextField(null=True)
