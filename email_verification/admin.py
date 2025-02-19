from django.contrib import admin
from email_verification.models import Email
# Register your models here.


@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ["id", "email", "count"]
