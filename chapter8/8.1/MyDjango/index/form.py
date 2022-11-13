from django import forms
from .models import *
class VocationForm(forms.Form):
    job = forms.CharField(max_length=20, label='职位')
    title = forms.CharField(max_length=20, label='职称')
    payment = forms.IntegerField(label='薪资')
    # 设置下拉框的值
    # 查询模型PersonInfo的数据
    value = PersonInfo.objects.values('name')
    # 将数据以为列表格式表示，列表元素为元组格式
    choices = [(i+1, v['name']) for i, v in enumerate(value)]
    # 表单字段设为ChoiceField类型，用生成下拉框
    person = forms.ChoiceField(choices=choices, label='姓名')
