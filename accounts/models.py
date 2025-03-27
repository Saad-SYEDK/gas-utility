# accounts/models.py
from django.contrib.auth.models import User
from django.db import models
from requests.models import ServiceRequest  # Importing request model

# Extend User model with profile info (if needed)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True)