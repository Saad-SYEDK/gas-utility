from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ServiceRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in progress', 'In Progress'),
        ('resolved', 'Resolved'),
        
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.request_type} ({self.status})"