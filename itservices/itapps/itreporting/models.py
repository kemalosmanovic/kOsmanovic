from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
# Create your models here.

    
class Product(models.Model):
    prod_name = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)
    avg_cost = models.FloatField()
    category = models.CharField(max_length=20)
    date_released = models.DateField(null=True, blank=True)
    description = models.CharField(max_length=50)
    image = models.ImageField(upload_to='product_pics')
    def __str__(self):
            return self.prod_name
    def get_absolute_url(self):
            return reverse('product-detail', kwargs={'pk': self.pk})

class Review(models.Model):
    author_name=models.ForeignKey(User, on_delete=models.CASCADE)
    id2=models.ForeignKey(Product, on_delete=models.CASCADE)
    RATING_CHOICES = [(str(i), str(i)) for i in range(1, 6)]
    rating = models.CharField(max_length=1, choices=RATING_CHOICES, default='1')
    details=models.TextField()
    date_reviewed=models.DateTimeField(default=timezone.now)
    def __str__(self):
            return self.author_name.username

    def get_absolute_url(self):
            return reverse('review-detail', kwargs={'pk': self.pk})
