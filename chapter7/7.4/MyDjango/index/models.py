from django.db import models

class City(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    class Meta:
        # 设置模型所属的App，从而在相应的数据库里生成数据表
        # 如不设置app_label，则默认当前文件所在的App
        app_label = "index"
        # 自定义数据表名称
        db_table = 'city'
        # 定义数据表在Admin后台的显示名称
        verbose_name = '城市信息表'