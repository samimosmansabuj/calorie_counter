from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator

# Create your models here.
class Custom_User(AbstractUser):
    username = models.CharField(max_length=50, validators=[UnicodeUsernameValidator], unique=True)
    email = models.EmailField(max_length=200, unique=True, blank=True, null=True)
    phone_number = models.CharField(max_length=14, blank=True, null=True)
    password = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.username



