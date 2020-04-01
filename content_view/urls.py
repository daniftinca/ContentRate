from django.conf.urls import url

from content_view import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^$', views.login, name='login'),
    url(r'^$', views.register, name='register'),
]