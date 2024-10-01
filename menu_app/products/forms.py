from django import forms
from .models import Category, Products

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('category_name', 'category_description', 'category_featured_image')
        labels = {
            'category_name': 'Nombre',
            'category_description': 'Descripción',
            'category_featured_image': 'Imagen',
        }