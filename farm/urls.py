from django.urls import path
from . import views

app_name = 'farm'
urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile_update, name='profile_update'),
    path('worker/new/', views.worker_create, name='worker_create'),
]