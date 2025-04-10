from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm

def signup_view(request):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('feed') 
    return render(request, 'authentication/signup.html', {'form': form})

def landing_view(request):
    form = AuthenticationForm()
    return render(request, 'authentication/landing.html', {'form': form})


