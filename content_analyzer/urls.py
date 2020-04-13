from content_analyzer.views import ContentAnalyserView
from django.conf.urls import url

app_name = 'content_analyzer'
urlpatterns = [
    url(r'^analyse', ContentAnalyserView.as_view()),
]
