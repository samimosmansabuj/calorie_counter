from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.contrib import messages
from .models import Calorie_Counter_Model, Date_Model
from django.utils import timezone
from django.contrib.auth.decorators import login_required


#------------Add Caleroie Function Start------------
@login_required
def calculate_calorie(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')
        
        user = request.user
        calorie_form = Calorie_Counter_Form(request.POST)
        if calorie_form.is_valid():
            calorie = calorie_form.save()
            
            calorie.user = user
            calorie.save()
            return redirect('dashboard')
        else:
            messages.error(request, calorie_form.errors)
            return redirect(request.META['HTTP_REFERER'])
    else:
        return redirect('dashboard')
#------------Add Caleroie Function End------------

#------------Home Start------------
def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    context = {}
    form = Calorie_Counter_Form()
    context['form'] = form
            
    return render(request, 'index.html', context)
#------------Home End------------

#------------Update Caleroie Start------------
@login_required
def udpate_calorie(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    
    calorie_instance = get_object_or_404(Calorie_Counter_Model, id=id)
    context = {}
    calorie_form = Calorie_Counter_Form(instance=calorie_instance)
    context['calorie_form'] = calorie_form
    
    if request.method == 'POST':
        calorie_form = Calorie_Counter_Form(request.POST, instance=calorie_instance)
        if calorie_form.is_valid():
            calorie = calorie_form.save(commit=False)
            calorie.save()
            return redirect('dashboard')
        else:
            messages.error(request, calorie_form.errors)
            return redirect(request.META['HTTP_REFERER'])
        
    return render(request, 'update_calorie.html', context)
#------------Update Caleroie End------------


def add_item(request):
    return None

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
        
        item_form = Iteam_Calorie_Form(request.POST)
        if item_form.is_valid():
            item = item_form.save()
            item.user = user
            item.date = date_model
            item.save()
        
        total_calorie = 0
        for i in date_model.item_date.all():
            calorie = i.calorie
            total_calorie+=calorie
        date_model.need_calorie = user_calorie.total_calorie
        date_model.today_total_calorie = total_calorie
        date_model.save()
        
        return redirect(request.META['HTTP_REFERER'])
               
    return render(request, 'dashboard.html', context)


