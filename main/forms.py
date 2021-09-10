from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    # title = forms.CharField(max_length=120)
    class Meta:
        model = Product
        fields = ('title', 'link', 'price')


