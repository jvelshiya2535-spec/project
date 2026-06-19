from django.db import models

# Create your models here.
class author(models.Model):
    name=models.CharField(max_length=150)
    email=models.EmailField()
    country=models.CharField(max_length=150)

def __str__(self):
    return self.name 