from django.contrib.auth import get_user_model
from .models import Product
from django import forms

class ProductCreationForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('tag', 
                'name',
                'description',
                'photo',
                )