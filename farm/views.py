from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm

def home(request):
    if request.user.is_authenticated:
        tasks = Task.objects.filter(user=request.user)
    else:
        tasks = None
    return render(request, 'farm/home.html', {'tasks': tasks})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('farm:home')
    else:
        form = UserCreationForm()
    return render(request, 'farm/register.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('farm:home')

@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('farm:home')
    else:
        form = TaskForm()
    return render(request, 'farm/task_form.html', {'form': form, 'action': 'Create'})

@login_required
def task_update(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('farm:home')
    else:
        form = TaskForm(instance=task)
    return render(request, 'farm/task_form.html', {'form': form, 'action': 'Update'})

@login_required
def task_delete(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('farm:home')
    return render(request, 'farm/task_confirm_delete.html', {'task': task})