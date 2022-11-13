from django import forms
from .models import *
class PersonInfoForm(forms.ModelForm):
    class Meta:
        model = PersonInfo
        fields = '__all__'
        labels = {
            'name': '姓名',
            'age': '年龄',
        }
