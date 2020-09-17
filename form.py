from django import forms
from .models import Todos

class listform(forms.ModelForm):
    class Meta:
        
        model=Todos
        fields=["title","desc","finish","date"]