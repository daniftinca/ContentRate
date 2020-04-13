from django.urls import path, include
from rest_framework import routers

from registration.views import UserRegistrationView, UserLoginView
from . import views

from django.conf.urls import url

app_name = 'registration'
urlpatterns = [
    url(r'^register', UserRegistrationView.as_view()),
    url(r'^login', UserLoginView.as_view()),
]
