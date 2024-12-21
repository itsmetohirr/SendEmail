import smtplib
from django.contrib import admin
from .models import UserNotification
from email_notification_project.settings import EMAIL_HOST_USER, EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_PASSWORD


@admin.register(UserNotification)
class UserNotificationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if not change:
            with smtplib.SMTP_SSL(EMAIL_HOST, EMAIL_PORT) as smtp_server:
                smtp_server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
                smtp_server.sendmail(EMAIL_HOST_USER, obj.email, obj.message)
            print(f"A new UserNotification was created: \n email: {obj.email}")
