from django import forms
from .models import Table1

class PostForm(forms.ModelForm):
    class Meta:
        model=Table1
        fields='__all__'
