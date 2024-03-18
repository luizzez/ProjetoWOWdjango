from django.apps import AppConfig


class CarroConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'carro'

    def ready(self):
        from .models import Usuario
        import os


