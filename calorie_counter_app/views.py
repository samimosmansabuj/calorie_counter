from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.contrib import messages
from .models import Calorie_Counter_Model, Date_Model
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def calculate_calorie(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')
        
        user = request.user
        calorie_form = Calorie_Counter_Form(request.POST)
        if calorie_form.is_valid():
            calorie = calorie_form.save()
            
            age = calorie_form.cleaned_data.get('age')
            height = calorie_form.cleaned_data.get('height')
            weight = calorie_form.cleaned_data.get('weight')
            gender = calorie_form.cleaned_data.get('gender')
            if gender == 'Male':
                BMR = 66.47 + (13.75 * float(height)) + (5.003 * float(weight)) - (6.755 * age)
            elif gender == 'Female':
                BMR = 655.1 + (9.563 * float(height)) + (1.850 * float(weight)) - (4.676 * age)
            
            calorie.user = user
            calorie.total_calorie = BMR
            calorie.save()
            return redirect('dashboard')
        else:
            messages.error(request, calorie_form.errors)
            return redirect(request.META['HTTP_REFERER'])
    else:
        return redirect('dashboard')


def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    context = {}
    form = Calorie_Counter_Form()
    context['form'] = form
            
    return render(request, 'index.html', context)

@login_required
def udpate_calorie(request, id):
    user = request.user
    calorie_instance = get_object_or_404(Calorie_Counter_Model, id=id)
    context = {}
    calorie_form = Calorie_Counter_Form(instance=calorie_instance)
    context['calorie_form'] = calorie_form
    
    if request.method == 'POST':
        calorie_form = Calorie_Counter_Form(request.POST, instance=calorie_instance)
        if calorie_form.is_valid():
            calorie = calorie_form.save(commit=False)
            
            age = calorie_form.cleaned_data.get('age')
            height = calorie_form.cleaned_data.get('height')
            weight = calorie_form.cleaned_data.get('weight')
            gender = calorie_form.cleaned_data.get('gender')
            
            if calorie_instance.gender == 'Male':
                BMR = 66.47 + (13.75 * float(height)) + (5.003 * float(weight)) - (6.755 * age)
            elif calorie_instance.gender == 'Female':
                BMR = 655.1 + (9.563 * float(height)) + (1.850 * float(weight)) - (4.676 * age)
            
            calorie.total_calorie = BMR
            calorie.save()
            
            return redirect('dashboard')
    return render(request, 'update_calorie.html', context)
    
@login_required
def dashboard(request):
    user = request.user
    context = {}
    calorie_form = Calorie_Counter_Form()
    context['calorie_form'] = calorie_form
    
    if Calorie_Counter_Model.objects.filter(user=user).exists():
        user_calorie = Calorie_Counter_Model.objects.get(user=user)
        context['user_calorie'] = user_calorie
    
    if Date_Model.objects.filter(user=user).exists():
        daily = Date_Model.objects.filter(user=user)
        context['daily'] = daily
    
    item_form = Iteam_Calorie_Form()
    context['item_form'] = item_form
    
    if request.method == 'POST':
        date_input = request.POST['date_input']
        if date_input:
            date = date_input
        else:
            date = timezone.now().date()
        
        if Date_Model.objects.filter(user=user, date=date):
            date_model = Date_Model.objects.get(user=user, date=date)
        else:
            date_model = Date_Model.objects.create(
                user=user, date=date
            )
            date_model.need_calorie = user_calorie.total_calorie
        
        item_form = Iteam_Calorie_Form(request.POST)
        if item_form.is_valid():
            item = item_form.save()
            item.user = user
            item.date = date_model
            item.save()
        
        total_calorie = date_model.today_total_calorie
        for i in date_model.item_date.all():
            calorie = i.calorie
            total_calorie+=calorie
        date_model.need_calorie = user_calorie.total_calorie
        date_model.today_total_calorie = total_calorie
        date_model.save()
        
        return redirect(request.META['HTTP_REFERER'])
               
    return render(request, 'dashboard.html', context)

def registration(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if User.objects.filter(username=username).exists():
            messages.warning(request, 'Username is already taken1')
            return redirect(request.META['HTTP_REFERE'])
        elif password != confirm_password:
            messages.warning(request, "Password & Confirm Password doesn't match!")
            return redirect(request.META['HTTP_REFERE'])
        else:
            user = User.objects.create_user(username=username, password=password)
            user.email = email
            user.save()
            return redirect('login')
        
    return render(request, 'registration.html')

def Login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if not User.objects.filter(username=username).exists():
            messages.warning(request, "Username Doesn't Match")
            return redirect(request.META['HTTP_REFERER'])
        else:
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.warning(request, "Password Doesn't Match")
                return redirect(request.META['HTTP_REFERER'])
    return render(request, 'login.html')

def Logout(request):
    logout(request)
    return redirect('login')
