import os


   
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "framework.settings")

#os.environ["DJANGO_SETTINGS_MODULE"] = "beachnbeach.settings"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
