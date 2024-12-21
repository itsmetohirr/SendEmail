from django.contrib import admin
from .models import UserNotification


@admin.register(UserNotification)
class UserNotificationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if not change:
            print(f"A new UserNotification was created: \n email: {obj.email}")
