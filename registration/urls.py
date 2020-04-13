from django.urls import path, include
from rest_framework import routers

from registration.views import UserRegistrationView, UserLoginView
from . import views

from django.conf.urls import url

app_name = 'registration'

#router = routers.SimpleRouter()
#router.register(r'/signup', UserRegistrationView)
#router.register(r'/login', UserLoginView)
urlpatterns = [
    #url(r'^', include(router.urls))
    url(r'^register', UserRegistrationView.as_view()),
    url(r'^login', UserLoginView.as_view()),
    #path('', views.user_register, name='user_register'),
]
