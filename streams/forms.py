
from django import forms

class SettingsForm(forms.form):
    stream_name = forms.CharField()
    stream_key = forms.CharField()
    description = forms.CharField()
