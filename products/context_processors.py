from .models import Category, Product


def get_categories(request):
    categories = Category.objects.all()
    return dict(categories=categories)


def get_products(request):
    products = Product.objects.all()
    return dict(products=products)