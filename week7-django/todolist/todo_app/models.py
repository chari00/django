from django.db import models

# Create your models here.

# Here is an example of a basic model class that represents a 'Post' in the blog:
class Task(models.Model):
    title = models.CharField(max_length=100)  # Title of the post
    description = models.TextField()  # Content of the post
    completed = models.DateTimeField(auto_now_add=True)  # Date of publication

    def __str__(self):
        return self.title
