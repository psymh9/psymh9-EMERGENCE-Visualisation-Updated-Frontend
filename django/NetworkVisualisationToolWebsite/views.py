from django.shortcuts import render
from pathlib import Path 
from django.conf import settings
from django.shortcuts import redirect
import subprocess, os
import time

# Create your views here.

def home(request):
    return render(request, "NetworkVisualisationToolWebsite/home.html", {})

def about(request):
    return render(request, "NetworkVisualisationToolWebsite/about.html", {})

def howto(request):
    return render(request, "NetworkVisualisationToolWebsite/how-to.html", {})

def test(request):
    return render(request, "NetworkVisualisationToolWebsite/PythonNetworkVisualisation.html", {})

def applyFiltrationOptions(request, filterCategory1, filterParameter1, filterCategory2, filterParameter2):
    if request.method == "GET":
        filterCategory1 = request.GET.get('filterCategory1')
        filterParameter1 = request.GET.get('filterParameter1')
        filterCategory2 = request.GET.get('filterCategory2')
        filterParameter2 = request.GET.get('filterParameter2')
    networkVisualisationScript = "NetworkVisualisationToolWebsite/templates/NetworkVisualisationToolWebsite/NetworkVisualisationToolUpdated.py"
    process = subprocess.Popen(['Python', networkVisualisationScript, filterCategory1, filterParameter1, 
                      filterCategory2, filterParameter2])
    time.sleep(4)
    return redirect('home')

def resetFiltrationOptions(request):
    networkVisualisationScript = "NetworkVisualisationToolWebsite/templates/NetworkVisualisationToolWebsite/NetworkVisualisationToolUpdated.py"
    process = subprocess.Popen(['Python', networkVisualisationScript])
    time.sleep(4)
    return redirect('home')
 
    

