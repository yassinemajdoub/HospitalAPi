from django.contrib import admin

from .models import Patient


# Register your models here.
@admin.register(Patient)
class PostAdmin(admin.ModelAdmin):
    list_display = ["email", "created"]
    list_filter = ["created"]
