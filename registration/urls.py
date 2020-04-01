from django.contrib import auth
from django.urls import path
from django.contrib.auth import views

from . import views

app_name = 'registration'
urlpatterns = [
    path('', views.custom_registration, name='custom_registration'),
    path('login/', views.custom_login, name='custom_login'),
    path('logout/', auth.views.LogoutView.as_view(), name='logout'),
]