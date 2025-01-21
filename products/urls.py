from django.urls import path
from . import category_views, product_views

urlpatterns = [

    path('categories/', category_views.category_list, name='category_list'),
    path('categories/<int:pk>/', category_views.category_detail, name='category_detail'),
    path('products/', product_views.product_list, name='product_list'),
    path('products/<int:pk>', product_views.product_detail, name='product_detail'),
]