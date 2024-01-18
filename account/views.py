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
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            login(request,user)
            return redirect('dashboard')
        else:
            messages.warning(request, login_form.errors)
            return redirect(request.META['HTTP_REFERER'])
        
    # if request.method == 'POST':
    #     username = request.POST['username']
    #     password = request.POST['password']
    #     if not Custom_User.objects.filter(username=username).exists():
    #         messages.warning(request, "Username Doesn't Match")
    #         return redirect(request.META['HTTP_REFERER'])
    #     else:
    #         user = authenticate(username=username, password=password)
    #         if user:
    #             login(request, user)
    #             return redirect('dashboard')
    #         else:
    #             messages.warning(request, "Password Doesn't Match")
    #             return redirect(request.META['HTTP_REFERER'])
    
    return render(request, 'account/login.html', {'login_form': login_form})

def Logout(request):
    logout(request)
    return redirect('login')
