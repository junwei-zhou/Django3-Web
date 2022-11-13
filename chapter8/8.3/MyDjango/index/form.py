from django import forms
from .models import *

class VocationForm(forms.ModelForm):
    # 添加模型外的表单字段
    LEVEL = (('L1', '初级'),
             ('L2', '中级'),
             ('L3', '高级'),)
    level = forms.ChoiceField(choices=LEVEL, label='级别')
    # 模型与表单设置
    class Meta:
        # 绑定模型
        model = Vocation
        # fields属性用于设置转换字段，'__all__'是将全部模型字段转换成表单字段
        # fields = '__all__'
        # fields = ['job', 'title', 'payment', 'person']
        # exclude用于禁止模型字段转换表单字段
        exclude = []
        # labels设置HTML元素控件的label标签
        labels = {
            'job': '职位',
            'title': '职称',
            'payment': '薪资',
            'person': '姓名'
        }
        # 定义widgets，设置表单字段的CSS样式
        widgets = {
            'job': forms.widgets.TextInput(attrs={'class': 'c1'}),
        }
        # 重新定义字段类型
        # 一般情况下模型字段会自动转换成表单字段
        field_classes = {
            'job': forms.CharField
        }
        # 帮助提示信息
        help_texts = {
            'job': '请输入职位名称'
        }
        # 自定义错误信息
        error_messages = {
            # __all__设置全部错误信息
            '__all__': {'required': '请输入内容',
                        'invalid': '请检查输入内容'},
            # 设置某个字段的错误信息
            'title': {'required': '请输入职称',
                      'invalid': '请检查职称是否正确'}
        }
    # 自定义表单字段payment的数据清洗
    def clean_payment(self):
        # 获取字段payment的值
        data = self.cleaned_data['payment'] + 1
        return data
