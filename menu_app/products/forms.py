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


class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ('product_name', 'product_price', 'category', 'product_description', 'product_featured_image')
        labels = {
            'product_name':'Nombre',
            'product_price': 'Precio',
            'category': 'Categoría',
            'product_description': 'Descripcion',
            'product_featured_image': 'Imagen'
        }