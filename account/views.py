from django.shortcuts import render, redirect
from django.contrib import messages
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import *

# Create your views here.
def registration(request):
    user_creation_form = User_Form()
    
    if request.method == 'POST':
        user_creation_form = User_Form(request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()
            return redirect('login')
        else:
            messages.warning(request, user_creation_form.errors)
            return redirect(request.META['HTTP_REFERER'])
        
    return render(request, 'account/registration.html', {'user_creation_form': user_creation_form})

def Login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    login_form = Login_Form()
    
    if request.method == 'POST':
        login_form = Login_Form(data=request.POST)
        if login_form.is_valid():
            login(request,login_form.get_user())
            return redirect('dashboard')
        else:
            messages.warning(request, login_form.errors)
            return redirect(request.META['HTTP_REFERER'])
    return render(request, 'account/login.html', {'login_form': login_form})

def Logout(request):
    logout(request)
    return redirect('login')
