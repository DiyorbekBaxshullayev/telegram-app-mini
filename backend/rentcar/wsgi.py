import os
import sys

path = '/home/DiyorbekBaxshullayev/telegram-app-mini/backend'
if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'rentcar.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
