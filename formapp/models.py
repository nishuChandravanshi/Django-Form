from django.db import models

# Create your models here.

class User(models.Model):
    first_name= models.CharField(max_length=150)
    last_name= models.CharField(max_length=150)
    email  =models.EmailField(max_length=150,unique=True)
