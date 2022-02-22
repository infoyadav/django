from django.apps import AppConfig


class DashbConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dashb'

    # def ready(self):
        # from dashb import signal
