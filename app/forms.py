from django import forms

class Calculate(forms.Form):
    value = forms.IntegerField()

