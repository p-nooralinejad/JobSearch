from django.db import models

# Create your models here.

class employer(models.Model):
    name = models.CharField(max_length=200)
    opening = models.IntegerField();
    pswd = models.CharField(max_length=40)
    addr = models.CharField(max_length=2000)
    phone = models.CharField(max_length=20)

class employee(models.Model):
    first_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    pswd = models.CharField(max_length=50)
    gender = models.CharField(max_length=1) #'F' or 'M'
    age = models.IntegerField()


