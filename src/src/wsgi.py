"""
WSGI config for src project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
import sys

#sys.path.append('/opt/rep/calorie-accounting/src')
#sys.path.append('/opt/rep/calorie-accounting/src/src')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "src.settings")

application = get_wsgi_application()
