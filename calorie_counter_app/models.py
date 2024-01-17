from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Calorie_Counter_Model(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=GENDER, blank=True, null=True)
    height = models.DecimalField(max_digits=9, decimal_places=2)
    weight = models.DecimalField(max_digits=9, decimal_places=2)
    
    total_calorie = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    
    def __str__(self) -> str:
        return self.name


class Date_Model(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    need_calorie = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True, default=0)
    today_total_calorie = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True, default=0)
    def __str__(self) -> str:
        return f'{self.date}'


class Iteam_Calorie_Model(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    
    item = models.CharField(max_length=100)
    calorie = models.DecimalField(max_digits=9, decimal_places=2)
    date = models.ForeignKey(Date_Model, on_delete=models.CASCADE, blank=True, null=True, related_name='item_date')
    
    def __str__(self) -> str:
        return self.item


