from django import forms
from .models import *
class VocationForm(forms.ModelForm):
    class Meta:
        model = Vocation
        fields = '__all__'
        labels = {
            'job': '职位',
            'title': '职称',
            'payment': '薪资',
            'person': '姓名'
        }
        error_messages = {
            '__all__': {'required': '请输入内容',
                        'invalid': '请检查输入内容'},
        }
    # 自定义表单字段payment的数据清洗
    def clean_payment(self):
        data = self.cleaned_data['payment'] + 10
        return data
