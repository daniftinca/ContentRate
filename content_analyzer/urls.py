from django.urls import path

from content_analyzer.views import ContentAnalyserView
from . import views
from django.conf.urls import url

app_name = 'content_analyzer'
urlpatterns = [
    # path('', views.analyze_content, name='analyze_content'), ???
    url(r'^analyse', ContentAnalyserView.as_view()),
]
