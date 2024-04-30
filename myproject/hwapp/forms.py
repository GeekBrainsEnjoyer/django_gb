from django import forms

from .models import Producthwapp


class ProductForm(forms.ModelForm):
    class Meta:
        model = Producthwapp
        fields = ('__all__')
