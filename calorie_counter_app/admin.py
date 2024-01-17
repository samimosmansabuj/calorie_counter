from django.contrib import admin
from .models import Calorie_Counter_Model, Iteam_Calorie_Model, Date_Model

# Register your models here.
@admin.register(Calorie_Counter_Model)
class Calorie_Counter_Model_Admin(admin.ModelAdmin):
    list_display = ['name', 'age', 'gender', 'height', 'weight']
    list_filter = ['name', 'age', 'gender']

@admin.register(Iteam_Calorie_Model)
class Calorie_Counter_Model_Admin(admin.ModelAdmin):
    list_display = ['item', 'calorie', 'date']


admin.site.register(Date_Model)