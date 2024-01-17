from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('calculate-calorie/', calculate_calorie, name='calculate_calorie'),
    
    path('login/', Login, name='login'),
    path('logout/', Logout, name='logout'),
    path('registration/', registration, name='registration'),
]