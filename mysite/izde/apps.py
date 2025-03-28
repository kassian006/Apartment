from django.apps import AppConfig


class IzdeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'izde'

    def ready(self):
        import izde.signals
