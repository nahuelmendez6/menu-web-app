from importlib.resources import contents
from itertools import product
from unicodedata import category

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Category, Products
from .forms import CategoryForm, ProductForm
from django.db.models import Q


# Create your views here.
# ----------------------- VIEWS PARA MANEJAR CATEGORIAS ------------------------------------------------------
@login_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)     # Instanciamos el formulario de Categoria
        if form.is_valid():                 # Si el formulario se completo correctamente
            category = form.save(commit=False)
            category.local_owner = request.user
            category.save()
            return redirect('show_categories')

    form = CategoryForm()       # Si el formulario no se ha enviado, instanciamos para generarlo
    context = {
        'form': form,
    }
    return render(request, 'add_category.html', context)


def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('show_categories')
    form = CategoryForm()
    context = {
        'form':form,
        'category':category
    }
    return render(request, 'edit_category.html', context)


def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('show_categories')


def show_categories(request):
    return render(request, 'categories.html')

# ----------------------- VIEWS PARA MANEJAR PRODUCTOS ------------------------------------------------------
@login_required
def add_products(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            new_product = form.save(commit=False)
            new_product.local_owner = request.user
            new_product.save()
            return redirect('show_products')
    form = ProductForm()
    context = {
        'form':form,
    }
    return render(request, 'add_products.html', context)


def edit_product(request, pk):
    product = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('show_products')
    form = ProductForm()
    context = {
        'form':form,
        'product':product
    }
    return render(request, 'edit_category.html', context)


def delete_product(request, pk):
    product = get_object_or_404(Products, pk=pk)
    product.delete()
    return redirect('show_products')


def show_products(request):
    return render(request, 'products.html')