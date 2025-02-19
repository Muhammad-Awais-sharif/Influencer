from django.urls import path, include
from email_verification.views import index, get_all_emails, export_into_csv


urlpatterns = [
    path('', index, name="index"),
    path('get_all_emails/', get_all_emails, name='get_all_emails'),
    path('export_excel/', export_into_csv, name='export_excel'),
]
