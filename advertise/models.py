from django.db import models

# Create your models here.
from register.models import employer, employee

class Advertise(models.Model):
    owner = models.ForeignKey(employer, on_delete=models.CASCADE )
    applicant = models.ForeignKey(employee)
    title = models.CharField(max_length=300)
    img = models.ImageField()
    expiree_date = models.DateField()
    field = models.CharField(max_length=400)
    salary = models.IntegerField()
    hours = models.IntegerField()

