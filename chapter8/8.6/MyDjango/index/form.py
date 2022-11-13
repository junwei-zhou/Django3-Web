from django import forms
from .models import *
from django.core.exceptions import ValidationError
# 自定义数据验证函数
def payment_validate(value):
    if value > 30000:
        raise ValidationError('请输入合理的薪资')

class VocationForm(forms.Form):
    job = forms.CharField(max_length=20, label='职位')
    # 设置字段参数widget、error_messages
    title = forms.CharField(max_length=20, label='职称',
                            widget=forms.widgets.TextInput(attrs={'class': 'c1'}),
                            error_messages={'required': '职称不能为空'},)
    # 设置字段参数validators
    payment = forms.IntegerField(label='薪资',validators=[payment_validate])
    # 设置下拉框的值
    # 查询模型PersonInfo的数据
    value = PersonInfo.objects.values('name')
    # 将数据以为列表格式表示，列表元素为元组格式
    choices = [(i+1, v['name']) for i, v in enumerate(value)]
    # 表单字段设为ChoiceField类型，用生成下拉框
    person = forms.ChoiceField(choices=choices, label='姓名')

    # 自定义表单字段title的数据清洗
    def clean_title(self):
        # 获取字段title的值
        data = self.cleaned_data['title']
        return '初级' + data
