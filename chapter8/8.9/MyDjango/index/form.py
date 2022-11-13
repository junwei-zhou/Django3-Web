from django import forms
from .models import *

class PersonInfoForm(forms.ModelForm):
    certificate = forms.FileField(label='证件', allow_empty_file=True, widget=forms.ClearableFileInput(attrs={'multiple': True}))
    class Meta:
        model = PersonInfo
        fields = '__all__'
        labels = {
            'name': '名字',
            'age': '年龄',
        }