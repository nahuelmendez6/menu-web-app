from django import forms
from .models import Category, Products, DAYS_OF_THE_WEEK

class CategoryForm(forms.ModelForm):

    available_days = forms.MultipleChoiceField(
        choices=DAYS_OF_THE_WEEK,
        widget=forms.CheckboxSelectMultiple,
        label_suffix='Días disponibles'
    )

    available_time_start = forms.TimeField(
        widget=forms.TimeInput(attrs={'type':'time'}),
        label='Hora de inicio'
    )

    available_time_end = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time'}),
        label='Hora de cierre'
    )

    class Meta:
        model = Category
        fields = ('category_name', 'category_description', 'category_featured_image', 'available_days',
                  'available_time_start', 'available_time_end',)
        labels = {
            'category_name': 'Nombre',
            'category_description': 'Descripción',
            'category_featured_image': 'Imagen',
            'available_days':'Días disponibles',
            'available_time_start': 'Horario de comienzo',
            'available_time_end': 'Horario de cierre',
        }

    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get('available_time_start')
        end_time = cleaned_data.get('available_time_end')

        if start_time and end_time and start_time >= end_time:
            raise forms.ValidationError("El horario de inicio debe ser antes del horario de fin.")

        return cleaned_data



class ProductForm(forms.ModelForm):

    available_days = forms.MultipleChoiceField(
        choices=DAYS_OF_THE_WEEK,
        widget=forms.CheckboxSelectMultiple,
        label_suffix='Dias disponibles'
    )

    available_time_start = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time'}),
        label='Hora de inicio'
    )

    available_time_end = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time'}),
        label='Hora de cierre'
    )

    class Meta:
        model = Products
        fields = ('product_name', 'product_price', 'category', 'product_description', 'product_featured_image',
                  'available_days', 'available_time_start', 'available_time_end',)
        labels = {
            'product_name':'Nombre',
            'product_price': 'Precio',
            'category': 'Categoría',
            'product_description': 'Descripcion',
            'product_featured_image': 'Imagen',
            'available_days':'Días disponibles',
            'available_time_start': 'Horario de comienzo',
            'available_time_end': 'Horario de cierre',
        }


    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get('available_time_start')
        end_time = cleaned_data.get('available_time_end')

        if start_time and end_time and start_time >= end_time:
            raise forms.ValidationError("El horario de inicio debe ser antes del horario de fin.")

        return cleaned_data