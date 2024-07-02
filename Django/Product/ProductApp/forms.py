from django import forms
from ProductApp.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product #linking our form to model (inside the db)
        fields = '__all__'

