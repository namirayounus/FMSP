from django.contrib import admin
from .models import Task, Crop, Livestock, Finance, Profile, HealthLog

admin.site.register(Task)
admin.site.register(Crop)
admin.site.register(Livestock)
admin.site.register(Finance)
admin.site.register(Profile)
admin.site.register(HealthLog)