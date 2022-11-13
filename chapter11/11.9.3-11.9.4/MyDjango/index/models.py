from django.db import models

class TaskInfo(models.Model):
    id = models.AutoField(primary_key=True)
    task = models.CharField(max_length=50)