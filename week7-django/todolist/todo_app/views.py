from django.shortcuts import render, get_object_or_404, redirect
# from django.http import HttpResponse
from .models import Task
from .forms import TaskForm

def task_list(request):
    tasks = Task.objects.all()  # Retrieve all tasks from the database
    return render(request, 'todo_app/task_list.html', {'tasks': tasks})

def task_detail(request, id):
    task = get_object_or_404(Task, pk=id)  # Fetch the task by ID or return a 404 error if not found
    return render(request, 'todo_app/task_detail.html', {'task': task})

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'todo_app/task_form.html', {'form': form})

def task_edit(request, id):
    task = get_object_or_404(Task, pk=id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'todo_app/task_form.html', {'form': form})

def task_delete(request, id):
    task = get_object_or_404(Task, pk=id)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'todo_app/task_confirm_delete.html', {'task': task})

