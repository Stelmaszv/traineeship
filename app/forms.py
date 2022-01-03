from django import forms
from django.core.exceptions import ValidationError


class Calculate(forms.Form):
    value = forms.IntegerField()

