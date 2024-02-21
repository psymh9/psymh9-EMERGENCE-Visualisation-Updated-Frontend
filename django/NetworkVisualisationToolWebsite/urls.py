# NetworkVisualisationToolWebsite/urls.py
from django.urls import path
from NetworkVisualisationToolWebsite import views 

urlpatterns = [
    path("", views.home, name='home'),
    path("about/", views.about, name="about"),
    path("how-to/", views.howto, name="how-to"),
]
