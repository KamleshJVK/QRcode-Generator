"""
WSGI config for task1 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/

"""



import newrelic.agent
newrelic.agent.initialize('newrelic.ini')
newrelic.agent.register_application()
import os  
from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "yourSettingsFile.settings")  
application = get_wsgi_application()

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task1.settings')

application = get_wsgi_application()
