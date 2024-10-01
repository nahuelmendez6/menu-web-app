from unicodedata import category

from django.urls import path

from .views import add_category, show_categories

urlpatterns = [
    path('add_category/', add_category, name='add_category'),
    path('categories/', show_categories, name='show_categories'),
]