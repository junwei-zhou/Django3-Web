from django.db import models

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=20)
    user = models.IntegerField()

    def __str__(self):
        return self.name