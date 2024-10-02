from itertools import product
from unicodedata import category

from django.shortcuts import render, get_object_or_404

from products.models import Products, Category


# Create your views here.
def menu_categories(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'menu.html', context)


def menu_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Products.objects.filter(category=category)
    context = {
        'category': category,
        'products': products,
    }
    return render(request, 'menu_products.html', context)