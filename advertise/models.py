from django.db import models

# Create your models here.
from register.models import employer, employee

class advertise(models.Model):
    adv_id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(employer, on_delete=models.CASCADE )
    title = models.CharField(max_length=300)
    img = models.ImageField()
    expiree_date = models.DateField()
    field = models.CharField(max_length=400)
    salary = models.IntegerField()
    hours = models.IntegerField()
    Description = models.CharField(max_length=1000)

    def __str__(self):
        return str({'owner':self.owner.name\
                    ,'title': self.title\
                    ,'expiree_date': self.expiree_date\
                    ,'field': self.field\
                    ,'salary':self.salary\
                    ,'hours':self.hours\
                    ,'Description':self.Description})

class application(models.Model):
    app_id = models.AutoField(primary_key=True)
    adv_id = models.ForeignKey(advertise, on_delete=models.CASCADE)
    applicant = models.ForeignKey(employee, on_delete=models.DO_NOTHING)

