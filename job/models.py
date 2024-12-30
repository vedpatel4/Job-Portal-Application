from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    job_type = models.CharField(max_length=100)

def __str__(self):
    return self.title
