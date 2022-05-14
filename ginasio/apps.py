from django.apps import AppConfig


class GinasioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ginasio'

    def ready(self):
        import ginasio.signals