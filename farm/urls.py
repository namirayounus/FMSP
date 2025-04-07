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
    path('livestock/', views.livestock_list, name='livestock_list'),
    path('livestock/new/', views.livestock_create, name='livestock_create'),
    path('livestock/<int:livestock_id>/update/', views.livestock_update, name='livestock_update'),
    path('livestock/<int:livestock_id>/delete/', views.livestock_delete, name='livestock_delete'),
    path('livestock/<int:livestock_id>/health-log/new/', views.health_log_create, name='health_log_create'),
    path('livestock/<int:livestock_id>/health-log/<int:log_id>/update/', views.health_log_update, name='health_log_update'),
    path('livestock/<int:livestock_id>/health-log/<int:log_id>/delete/', views.health_log_delete, name='health_log_delete'),
    path('finances/', views.finance_list, name='finance_list'),
    path('finance/new/', views.finance_create, name='finance_create'),
    path('finance/<int:finance_id>/update/', views.finance_update, name='finance_update'),
    path('finance/<int:finance_id>/delete/', views.finance_delete, name='finance_delete'),
    path('profile/', views.profile_update, name='profile_update'),
    path('dashboard/', views.dashboard, name='dashboard'),
]