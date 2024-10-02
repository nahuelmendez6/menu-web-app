from collections import namedtuple

from django.urls import path

from .views import menu_categories, menu_products

urlpatterns = (
    path('menu_categories', menu_categories, name='menu_categories'),
    path('menu_products/<int:category_id>', menu_products ,name='menu_products')
)