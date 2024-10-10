from importlib.resources import contents
from itertools import product
from unicodedata import category
import pdb
from django.contrib.auth.decorators import login_required
from django.db.transaction import commit
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Category, Products
from .forms import CategoryForm, ProductForm
from django.db.models import Q


# Create your views here.
# ----------------------- VIEWS PARA MANEJAR CATEGORIAS ------------------------------------------------------
@login_required
@login_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            category = form.save(commit=False)
            category.local_owner = request.user
            category.save()
            return redirect('show_categories')
        else:
            print(form.errors)  # Para ver qué errores tiene el formulario
    else:
        form = CategoryForm()
    return render(request, 'add_category.html', {'form': form})


@login_required
def edit_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)  # Asegúrate de pasar la instancia
        if form.is_valid():
            form.save()
            #category.local_owner = request.user  # Asegúrate de asignar el propietario local
            #category.save()
            return redirect('show_categories')
        else:
            print(form.errors)  # Verifica qué errores hay en el formulario
    form = CategoryForm(instance=category)
    context = {
        'form':form,
        'category':category
    }
    return render(request, 'edit_category.html', context)



def delete_category(request, category_id):
    d_category = get_object_or_404(Category, pk=category_id)
    d_category.delete()
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
    return render(request, 'edit_products.html', context)


def delete_product(request, pk):
    product = get_object_or_404(Products, pk=pk)
    product.delete()
    return redirect('show_products')


def show_products(request):
    return render(request, 'products.html')