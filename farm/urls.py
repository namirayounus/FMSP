from django.urls import path
from . import views

app_name = 'farm'
urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('task/new/', views.task_create, name='task_create'),
    path('task/<int:task_id>/update/', views.task_update, name='task_update'),
    path('task/<int:task_id>/delete/', views.task_delete, name='task_delete'),
    path('crops/', views.crop_list, name='crop_list'),
    path('crop/new/', views.crop_create, name='crop_create'),
    path('crop/<int:crop_id>/update/', views.crop_update, name='crop_update'),
    path('crop/<int:crop_id>/delete/', views.crop_delete, name='crop_delete'),
]