from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('overdue', 'Overdue'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    worker = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_tasks')
    description = models.CharField(max_length=200)
    due_date = models.DateField()
    completed = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Automatically set status based on due date and completion
        today = timezone.now().date()
        if self.completed:
            self.status = 'completed'
        elif self.due_date < today and not self.completed:
            self.status = 'overdue'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.description
    
class Crop(models.Model):
    GROWTH_STAGES = [
        ('planted', 'Planted'),
        ('growing', 'Growing'),
        ('ready', 'Ready to Harvest'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    planting_date = models.DateField()
    harvest_date = models.DateField()
    notes = models.TextField(blank=True, null=True)
    growth_stage = models.CharField(max_length=20, choices=GROWTH_STAGES, default='planted', editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        today = timezone.now().date()
        created_date = self.created_at.date() if self.pk else today
        if today >= self.harvest_date:
            self.growth_stage = 'ready'
        elif today > self.planting_date:
            self.growth_stage = 'growing'
        else:
            self.growth_stage = 'planted'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class Livestock(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)  # e.g., "Cow", "Chicken"
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    health_status = models.CharField(max_length=100, default="Healthy")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.type})"
    
class HealthLog(models.Model):
    livestock = models.ForeignKey(Livestock, on_delete=models.CASCADE, related_name='health_logs')
    date = models.DateField()
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.livestock.name} - {self.date}"
    
class Inventory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.quantity})"
    
class Finance(models.Model):
    TRANSACTION_TYPES = [
        ('income', 'Income'),
        ('expense', 'Expense'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.transaction_type.capitalize()} - {self.amount}"
    
class Profile(models.Model):
    ROLE_CHOICES = [
        ('owner', 'Owner'),
        ('worker', 'Worker'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='owner')

    def __str__(self):
        return f"{self.user.username}'s Profile"