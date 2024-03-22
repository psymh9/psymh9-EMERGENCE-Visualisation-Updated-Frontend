from django.apps import AppConfig
import subprocess, time

class NetworkVisualisationToolWebsiteConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "NetworkVisualisationToolWebsite"
    def ready(self):
         networkVisualisationScript = "NetworkVisualisationToolWebsite/templates/NetworkVisualisationToolWebsite/NetworkVisualisationToolUpdated.py"
         process = subprocess.Popen(['Python', networkVisualisationScript])
         time.sleep(1.5)
