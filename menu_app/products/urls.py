from django.urls import path
from .views import add_category, show_categories, add_products, show_products, edit_category, delete_category

urlpatterns = [

    path('add_category/', add_category, name='add_category'),
    path('categories/', show_categories, name='show_categories'),
    path('edit_category', edit_category, name='edit_category'),
    path('delete_category', delete_category, name='delete_category'),

    path('add_products/', add_products, name='add_products'),
    path('show_products/', show_products, name='show_products')
]