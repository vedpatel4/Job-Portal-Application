from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.TextField()
    contact_number = models.CharField(max_length=10)
    email = models.EmailField()
    website= models.URLField(blank=True, null=True)

def __str__(self):
        return self.name

