from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    User_Type_Choices = (
        ('Patient', 'Patient'),
        ('Doctor', 'Doctor'),
    )
    
    
    
    city = models.CharField(max_length = 100)
    state = models.CharField(max_length = 100)
    pincode = models.CharField(max_length = 100)
    address = models.CharField(max_length = 100)
    user_type = models.CharField(max_length=8, choices=User_Type_Choices)
    profile_picture = models.ImageField(upload_to ='media/', blank=True)

