from django import forms
from .models import Task, Crop, Livestock, Finance

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['description', 'due_date', 'completed']
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