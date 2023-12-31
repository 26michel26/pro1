from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    bio=models.CharField(max_length=50)
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    picture=models.ImageField(upload_to="profile_picture")
    
# Create your models here.
