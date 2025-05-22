from django.apps import AppConfig
from django.contrib.auth.models import User
import logging

class BloodConfig(AppConfig):
    name = 'blood'

    def ready(self):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('susheel', 'susheel@gmail.com', 'CC123')
            logging.info("Superuser created: susheel")
