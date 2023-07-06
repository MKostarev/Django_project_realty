from django.apps import AppConfig


class IndexRequestConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'index_request'

    def ready(self):
        import sender.signals
