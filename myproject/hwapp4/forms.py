from django import forms

from .models import Producthwapp4


class ProductForm(forms.ModelForm):
    class Meta:
        model = Producthwapp4
        fields = ('__all__')
