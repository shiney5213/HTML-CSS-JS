from . import models
from django.forms import ValidationError
from django import forms

def validator(value):
    if len(value) < 5:
        raise ValidationError('길이가 너무 짧아요')

class MemoForm(forms.ModelForm):
    class Meta:
        model = models.Memo
        fields = ['title', 'text', 'category']

        def __init__(self, *args, **kwargs):
            super(MemoForm, self).__init__(*args, **kwargs)
            self.fields['title'].validator=[validator]