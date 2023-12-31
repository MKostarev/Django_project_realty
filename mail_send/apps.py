from django.apps import AppConfig


class MailSendConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mail_send'

    def ready(self):
        import mail_send.signals