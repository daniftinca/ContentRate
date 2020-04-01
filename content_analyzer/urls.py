from django.urls import path

from . import views
app_name = 'content_analyzer'
urlpatterns = [
    path('', views.analyze_content, name='analyze_content'),
]