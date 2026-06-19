from django.db import models
from author.models import author

# Create your models here.
class book(models.Model):
    author=models.ForeignKey(author,on_delete=models.CASCADE,related_name='book')
    title=models.TextField()
    category=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    published_date=models.DateField()

def __str__(self):
    return self.author  