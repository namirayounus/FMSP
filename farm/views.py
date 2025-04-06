from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Task, Crop, Livestock, Finance, Profile
from .forms import TaskForm, CropForm, LivestockForm, FinanceForm, ProfileForm
from django.utils import timezone
from datetime import timedelta

def home(request):
    if request.user.is_authenticated:
        tasks = Task.objects.filter(user=request.user)
        Profile.objects.get_or_create(user=request.user)
        today = timezone.now().date()
        two_days_from_now = today + timedelta(days=2)
        upcoming_tasks = Task.objects.filter(
            user=request.user,
            due_date__range=[today, two_days_from_now],
            completed=False
        )
    else:
        tasks = None
        upcoming_tasks = None
    return render(request, 'farm/home.html', {'tasks': tasks, 'upcoming_tasks': upcoming_tasks})

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

@login_required
def crop_list(request):
    crops = Crop.objects.filter(user=request.user)
    return render(request, 'farm/crop_list.html', {'crops': crops})

@login_required
def crop_create(request):
    if request.method == 'POST':
        form = CropForm(request.POST)
        if form.is_valid():
            crop = form.save(commit=False)
            crop.user = request.user
            crop.save()
            return redirect('farm:crop_list')
    else:
        form = CropForm()
    return render(request, 'farm/crop_form.html', {'form': form, 'action': 'Create'})

@login_required
def crop_update(request, crop_id):
    crop = Crop.objects.get(id=crop_id, user=request.user)
    if request.method == 'POST':
        form = CropForm(request.POST, instance=crop)
        if form.is_valid():
            form.save()
            return redirect('farm:crop_list')
    else:
        form = CropForm(instance=crop)
    return render(request, 'farm/crop_form.html', {'form': form, 'action': 'Update'})

@login_required
def crop_delete(request, crop_id):
    crop = Crop.objects.get(id=crop_id, user=request.user)
    if request.method == 'POST':
        crop.delete()
        return redirect('farm:crop_list')
    return render(request, 'farm/crop_confirm_delete.html', {'crop': crop})

@login_required
def livestock_list(request):
    livestock = Livestock.objects.filter(user=request.user)
    return render(request, 'farm/livestock_list.html', {'livestock': livestock})

@login_required
def livestock_create(request):
    if request.method == 'POST':
        form = LivestockForm(request.POST)
        if form.is_valid():
            livestock = form.save(commit=False)
            livestock.user = request.user
            livestock.save()
            return redirect('farm:livestock_list')
    else:
        form = LivestockForm()
    return render(request, 'farm/livestock_form.html', {'form': form, 'action': 'Create'})

@login_required
def livestock_update(request, livestock_id):
    livestock = Livestock.objects.get(id=livestock_id, user=request.user)
    if request.method == 'POST':
        form = LivestockForm(request.POST, instance=livestock)
        if form.is_valid():
            form.save()
            return redirect('farm:livestock_list')
    else:
        form = LivestockForm(instance=livestock)
    return render(request, 'farm/livestock_form.html', {'form': form, 'action': 'Update'})

@login_required
def livestock_delete(request, livestock_id):
    livestock = Livestock.objects.get(id=livestock_id, user=request.user)
    if request.method == 'POST':
        livestock.delete()
        return redirect('farm:livestock_list')
    return render(request, 'farm/livestock_confirm_delete.html', {'livestock': livestock})

@login_required
def finance_list(request):
    finances = Finance.objects.filter(user=request.user)
    return render(request, 'farm/finance_list.html', {'finances': finances})

@login_required
def finance_create(request):
    if request.method == 'POST':
        form = FinanceForm(request.POST)
        if form.is_valid():
            finance = form.save(commit=False)
            finance.user = request.user
            finance.save()
            return redirect('farm:finance_list')
    else:
        form = FinanceForm()
    return render(request, 'farm/finance_form.html', {'form': form, 'action': 'Create'})

@login_required
def finance_update(request, finance_id):
    finance = Finance.objects.get(id=finance_id, user=request.user)
    if request.method == 'POST':
        form = FinanceForm(request.POST, instance=finance)
        if form.is_valid():
            form.save()
            return redirect('farm:finance_list')
    else:
        form = FinanceForm(instance=finance)
    return render(request, 'farm/finance_form.html', {'form': form, 'action': 'Update'})

@login_required
def finance_delete(request, finance_id):
    finance = Finance.objects.get(id=finance_id, user=request.user)
    if request.method == 'POST':
        finance.delete()
        return redirect('farm:finance_list')
    return render(request, 'farm/finance_confirm_delete.html', {'finance': finance})

@login_required
def profile_update(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        if 'remove_picture' in request.POST:
            if profile.profile_picture:
                profile.profile_picture.delete(save=True)  # Deletes the file and clears the field
            return redirect('farm:home')
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('farm:home')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'farm/profile_form.html', {'form': form, 'profile': profile})