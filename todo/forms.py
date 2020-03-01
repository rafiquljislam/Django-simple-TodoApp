from django import forms
from django.forms import ModelForm
from .models import TodoItem

class TodoForm(forms.ModelForm):
    
    class Meta:
        model = TodoItem
        fields = "__all__"
