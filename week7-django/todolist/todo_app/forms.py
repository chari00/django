# forms.py
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'completed')  # Specify the fields we want in the form: 'title' and 'description'.
