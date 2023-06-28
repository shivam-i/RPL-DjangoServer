# forms.py
from django import forms

class MyForm(forms.Form):
    input_text = forms.CharField(max_length=100)
