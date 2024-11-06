# from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import path
from django.db import models
from .models import Task


# Create your views here.

# Let's create a view to display a list of blog posts.
def task_list(request):
    posts = Task.objects.all()  # Retrieve all posts from the database
    return HttpResponse(f"List of Posts: {posts}")  # Return a simple HttpResponse for demonstration
    # return render(request, 'blog/post_list.html', {'posts': posts})

# Now, let's create a view to display the details of a specific blog post based on its ID.
def task_detail(request, id):
    post = get_object_or_404(Task, pk=id)  # Fetch the post by ID or return a 404 error if not found
    return HttpResponse(f"Post Detail: {post}")  # Return a simple HttpResponse for demonstration
    # return render(request, 'blog/post_detail.html', {'post': post})

# Create a view to delete a specific blog post based on its ID.
def task_delete(request, id):
    post = get_object_or_404(Task, pk=id)  # Fetch the post by ID or return a 404 error if not found
    if request.method == 'POST':
        post.delete()  # Delete the post from the database
        return redirect('post_list')  # Redirect to the list of posts after deletion
    return HttpResponse(f"Post Delete: {post}")  # Return a simple HttpResponse for demonstration
    # return render(request, 'blog/post_confirm_delete.html', {'post': post})
