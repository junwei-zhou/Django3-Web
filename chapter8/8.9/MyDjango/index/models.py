from django.db import models
import os
from django.core.files.storage import FileSystemStorage
from django.conf import settings

class PersonInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    age = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '人员信息'


# 重写内置文件类FileSystemStorage，如果上存文件名已存在media文件夹，则删除原文件
class mystorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name


class CertificateInfo(models.Model):
    id = models.AutoField(primary_key=True)
    certificate = models.FileField(blank=True, upload_to='images/', storage=mystorage())
    person = models.ForeignKey(PersonInfo, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.person

    class Meta:
        verbose_name = '证件信息'
