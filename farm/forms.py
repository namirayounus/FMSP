from django import forms
from .models import Task, Crop, Livestock, Finance, Profile, HealthLog, Inventory

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['description', 'due_date', 'completed','status']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }

class CropForm(forms.ModelForm):
    class Meta:
        model = Crop
        fields = ['name', 'planting_date', 'harvest_date', 'notes']
        widgets = {
            'planting_date': forms.DateInput(attrs={'type': 'date'}),
            'harvest_date': forms.DateInput(attrs={'type': 'date'}),
        }

class LivestockForm(forms.ModelForm):
    class Meta:
        model = Livestock
        fields = ['type', 'name', 'birth_date', 'health_status']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }

class FinanceForm(forms.ModelForm):
    class Meta:
        model = Finance
        fields = ['transaction_type', 'amount', 'date', 'description']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture']

class HealthLogForm(forms.ModelForm):
    class Meta:
        model = HealthLog
        fields = ['date', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['name', 'quantity']