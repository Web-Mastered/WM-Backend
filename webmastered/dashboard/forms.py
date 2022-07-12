from django import forms

from business.models import Staff


class CustomStaffSettingsForm(forms.ModelForm):
    class Meta:
        model = Staff
        exclude = ["user"]
