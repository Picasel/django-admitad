import os
import sys

import django

abspath = lambda *p: os.path.abspath(os.path.join(*p))
PROJECT_ROOT = abspath(os.path.dirname(__file__))
ADMITAD_TESTS_MODULE_PATH = abspath(PROJECT_ROOT, '..')
sys.path.insert(0, ADMITAD_TESTS_MODULE_PATH)
os.environ["DJANGO_SETTINGS_MODULE"] = 'integration.settings'
django.setup()
