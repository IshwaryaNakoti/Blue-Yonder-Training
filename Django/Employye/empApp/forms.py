from django import forms
from django.core import validators

#custom validator
def startswith(value):
    if value[0].lower() != 'd':
        raise forms.ValidationError("Name should start with 'D' or 'd'")

class Student(forms.Form):
    name = forms.CharField(max_length=50, validators=[validators.MinLengthValidator(4), validators.MaxLengthValidator(8), startswith])
    age = forms.IntegerField()