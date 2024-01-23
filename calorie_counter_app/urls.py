from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('udpate-calorie/<int:id>/', udpate_calorie, name='udpate_calorie'),
    path('calculate-calorie/', calculate_calorie, name='calculate_calorie'),
    path('item-update/<int:pk>/', item_update, name='item_update'),
    path('item-delete/<int:pk>/', delete_item, name='delete_item'),
    
    
]