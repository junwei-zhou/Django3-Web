from django.db import models

# Create your models here.
class PersonInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    hireDate = models.DateField()