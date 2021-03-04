from django import forms
from home.models import Images


class ImageForm(forms.ModelForm):
    """ Form para el modelo images"""
    class Meta:
        model = Images
        fields = ('titulo', 'imagen') 
