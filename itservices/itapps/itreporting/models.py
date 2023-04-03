from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
# Create your models here.
class Issue(models.Model):
    author_name=models.ForeignKey(User, on_delete=models.CASCADE)
    productrating=models.IntegerField(
        null=False,
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    details=models.TextField()
    date_reviewed=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.type

    def get_absolute_url(self):
        return reverse('issue-detail', kwargs={'pk': self.pk})