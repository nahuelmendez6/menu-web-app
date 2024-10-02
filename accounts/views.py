from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth.models import Group
from django.contrib.auth import logout

# Create your views here.
def home(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='owners')
            group.user_set.add(user)
            return redirect('login')
    else:
        form = RegistrationForm()
    context = {
        'form':form
    }

    return render(request, 'register.html', context)


def login(request):
    form = AuthenticationForm(request, request.POST)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
            return redirect('home')
    context = {
        'form':form
    }
    return render(request, 'login.html', context)

def logout_view(request):
    logout(request)
    return redirect('home')