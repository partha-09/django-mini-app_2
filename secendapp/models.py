from django.db import models

# Create your models here.
class Information(models.Model):
    fullName = models.CharField(max_length=222)
    emial = models.EmailField(max_length=222)
    phone = models.CharField(max_length=15)  # Use CharField for phone numbers

