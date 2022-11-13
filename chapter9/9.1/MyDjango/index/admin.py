from django.contrib import admin
from .models import *


# 方法一：
# 将模型直接注册到admin后台
# admin.site.register(PersonInfo)

# 方法二：
# 自定义PersonInfoAdmin类并继承ModelAdmin
# 注册方法一，使用装饰器将PersonInfoAdmin和Product绑定
@admin.register(PersonInfo)
class PersonInfoAdmin(admin.ModelAdmin):
    # 设置显示的字段
    list_display = ['id', 'name', 'age']
# 注册方法二
# admin.site.register(PersonInfo, PersonInfoAdmin)
