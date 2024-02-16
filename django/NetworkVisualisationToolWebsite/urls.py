# NetworkVisualisationToolWebsite/urls.py
from django.urls import path
from NetworkVisualisationToolWebsite import views 

urlpatterns = [
    path("", views.home, name='home'),
]
