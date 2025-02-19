from django import forms
from email_verification.models import Email

import email_verification


# class EmailForm(forms.Form):
#     userEmail = forms.CharField(label='Enter user Email', required=True,
#                                 max_length=100, error_messages={'required': 'Please enter Email'})

class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = "__all__"
