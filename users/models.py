from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg
from django.urls import reverse
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=20, null=True, blank=True)
    city_or_town = models.CharField(max_length=20, null=True, blank=True)
    country = models.CharField(max_length=20, null=True, blank=True)
    def __str__(self):
        return f'Profile for {self.user.username}'

