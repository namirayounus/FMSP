from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout

def home(request):
    return render(request, 'farm/home.html')

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