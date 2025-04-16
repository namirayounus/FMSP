from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django import forms
from .models import Profile
from .forms import ProfileForm, WorkerCreationForm

def home(request):
    return render(request, 'farm/home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user, role='owner')  # Set as Owner
            login(request, user)
            return redirect('farm:home')
    else:
        form = UserCreationForm()
    return render(request, 'farm/register.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('farm:home')

@login_required
def profile_update(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request, 'farm/profile_form.html', {'profile': profile})

@login_required
def worker_create(request):
    if request.user.profile.role != 'owner':
        return redirect('farm:home')  # Only owners can access
    if request.method == 'POST':
        form = WorkerCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user, role='worker')  # Set as Worker
            return redirect('farm:home')
    else:
        form = WorkerCreationForm()
    return render(request, 'farm/worker_form.html', {'form': form})