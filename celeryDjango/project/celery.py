#after setting up the celery in setting.py

from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

app = Celery('project')
app.conf.enable_utc = False   #since we are using timezone asia/kathmandu not default
                              #as we set timezone utc as asia/kathmandu
app.conf.update(timezone='Asia/kathmandu')  
app.config_from_object(settings, namespace='CELERY')  

#CELERY BEAT SETTINGS

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    prints(f'request:{self.request!r}')