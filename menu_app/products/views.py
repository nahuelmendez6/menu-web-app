from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Category, Products
from .forms import CategoryForm
from django.db.models import Q


# Create your views here.
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


def show_categories(request):
    return render(request, 'categories.html')