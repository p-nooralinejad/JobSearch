from django.db import models

# Create your models here.

class employer(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    opening = models.IntegerField();
    pswd = models.CharField(max_length=40)
    addr = models.CharField(max_length=2000)
    phone = models.CharField(max_length=20)
    field = models.CharField(max_length=200)

class employee(models.Model):
    first_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    username = models.CharField(max_length=50, primary_key= True)
    pswd = models.CharField(max_length=50)
    gender = models.CharField(max_length=1) #'F' or 'M'
    age = models.IntegerField()
    field = models.CharField(max_length=200)
    def __str__(self):
        return str({'name' : self.first_name + ' ' + self.surname\
                    ,'username': self.username\
                    ,'gender': self.gender\
                    ,'age': self.age})
