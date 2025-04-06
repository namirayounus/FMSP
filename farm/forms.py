from django import forms
from .models import Task

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