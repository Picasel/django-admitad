import os
import sys

import django

os.environ["DJANGO_SETTINGS_MODULE"] = 'tests.settings'
django.setup()
