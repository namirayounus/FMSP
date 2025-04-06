from django.contrib import admin
from .models import Task, Crop, Livestock

admin.site.register(Task)
admin.site.register(Crop)
admin.site.register(Livestock)