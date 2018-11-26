import os

import django

os.environ["DJANGO_SETTINGS_MODULE"] = 'tests.integration.settings'
django.setup()
