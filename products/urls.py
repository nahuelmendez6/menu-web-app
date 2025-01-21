from django.urls import path
from . import category_views, product_views

urlpatterns = [

    path('v1/categories/', category_views.category_list, name='category_list'),
    path('v1/categories/<int:pk>/', category_views.category_detail, name='category_detail'),
    path('v1/products/', product_views.product_list, name='product_list'),
    path('v1/products/<int:pk>', product_views.product_detail, name='product_detail'),
]