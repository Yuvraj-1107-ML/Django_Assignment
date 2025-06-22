# your_project/celery.py

import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Core.settings')

app = Celery('Core')

# Load task modules from all registered Django apps
app.config_from_object('django.conf:settings', namespace='CELERY')


app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
