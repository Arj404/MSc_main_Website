from django import forms
from models import Registration


class Register(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ('name', 'email', 'number', 'year')
