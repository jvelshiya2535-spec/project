from django.db import models

# Create your models here.
class file(models.Model):
    name=models.CharField(max_length=150)
    email=models.EmailField()
    phone_number=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

def __str__(self):
    return self.name   