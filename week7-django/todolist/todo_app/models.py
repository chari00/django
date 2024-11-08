
# models.py
from django import forms
from django.db import models
from django.utils import timezone

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title


class PostForm(forms.ModelForm):
    # Meta class is used to specify the model and fields we want to include in the form.
    class Meta:
        model = Task  # Link the form to the Task model.
        fields = ('title', 'description', 'completed')  # Specify the fields we want in the form: 'title' and 'description'.
