from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model): 
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class Lesson(models.Model):
    name = models.CharField(max_length=200)
    URL = models.URLField()
    length = models.SmallIntegerField()
    inProduct = models.ManyToManyField(Product)