from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "NetworkVisualisationToolWebsite/home.html", {})

def about(request):
    return render(request, "NetworkVisualisationToolWebsite/about.html", {})

def howto(request):
    return render(request, "NetworkVisualisationToolWebsite/how-to.html", {})
