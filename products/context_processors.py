from .models import Category, Products


def get_categories(request):
    categories = Category.objects.all()
    return dict(categories=categories)


def get_products(request):
    products = Products.objects.all()
    return dict(products=products)