# Generated by Django 5.2 on 2025-04-06 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0005_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('in_progress', 'In Progress'), ('completed', 'Completed'), ('overdue', 'Overdue')], default='pending', max_length=20),
        ),
    ]
