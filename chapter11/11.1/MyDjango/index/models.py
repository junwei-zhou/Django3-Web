from django.db import models


class Product(models.Model):
    id = models.AutoField('序号', primary_key=True)
    name = models.CharField('名称', max_length=50)
    slogan = models.CharField('简介', max_length=50)
    sell = models.CharField('宣传', max_length=50)
    price = models.IntegerField('价格')
    photo = models.CharField('相片', max_length=50)

    # 设置返回值
    def __str__(self):
        return self.name
