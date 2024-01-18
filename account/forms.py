from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import Custom_User

class Login_Form(AuthenticationForm):
    username = forms.CharField(max_length=50, label='Username', widget=forms.TextInput(attrs={
        'placeholder': 'Enter Username', 'class': 'form-control'
    }))
    password = forms.CharField(label='Password', max_length=50, widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password', 'class': 'form-control'
    }))



class User_Form(UserCreationForm):
    username = forms.CharField(max_length=50, label='Username', widget=forms.TextInput(attrs={
        'placeholder': 'Enter Username', 'class': 'form-control'
    }))
    email = forms.EmailField(label='Email Address', widget=forms.EmailInput(attrs={
        'placeholder': 'Enter Email Address', 'class': 'form-control'
    }))
    phone_number = forms.CharField(label='Phone Number', widget=forms.TextInput(attrs={
        'placeholder': 'Enter Phone Number', 'class': 'form-control'
    }))
    password1 = forms.CharField(label='Password', max_length=50, widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password', 'class': 'form-control'
    }))
    password2 = forms.CharField(
        label='Confirm Password',
        help_text=("Enter the same password as before, for verification."),
        max_length=50, widget=forms.PasswordInput(attrs={
            'placeholder': 'Enter Confirm Password', 'class': 'form-control'
        })
    )
    
    class Meta:
        model = Custom_User
        fields = ['username', 'email', 'phone_number']




