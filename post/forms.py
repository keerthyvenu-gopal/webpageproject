from .models import post
from django import forms
class ModelForm(forms.ModelForm):
    class Meta:
        model=post
        fields=['title','desc','img']