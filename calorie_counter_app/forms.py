from django import forms
from .models import Calorie_Counter_Model, Iteam_Calorie_Model

class Iteam_Calorie_Form(forms.ModelForm):
    class Meta:
        model = Iteam_Calorie_Model
        fields = ['item', 'calorie']
        widgets = {
            'item': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter Item Name'}
            ),
            'calorie': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter Item Calorie'}
            ),
        }


class Calorie_Counter_Form(forms.ModelForm):
    
    class Meta:
        model = Calorie_Counter_Model
        fields = ['name', 'age', 'gender', 'height', 'weight']
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter Your Name'}
            ),
            'age': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter Your Age'}
            ),
            'gender': forms.Select(
                attrs={'class': 'form-control'}
            ),
            'height': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter Your Height in cm'}
            ),
            'weight': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter Your Weight in kg'}
            ),
        }