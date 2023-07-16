
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from managers.models import Managers
from request.models import Rerust


@receiver(post_save, sender=Rerust)
def send_email_to_manager(sender, instance, created, **kwargs):
    if created:
        sudject = 'Новая заявка'
        message = f"Новая заявка:\n\nИмя: {instance.name}\nEmail: {instance.email}\nВопрос: {instance.question}"
        #message = f"A new request"
        from_email = 'mikh.kostarev@yandex.ru'
        recipient_list = ['hangdi1990@gmail.com']
        #recipient_list = {}
        send_mail(sudject, message, from_email, recipient_list)


@receiver(post_save, sender=Rerust)
def send_email_to_manager(sender, instance, created, **kwargs):
    if created:
        sudject = 'Заявка принята'
        message = f"Заявка принята:\n\nИмя: {instance.name}\nEmail: {instance.email}\nВопрос: {instance.question}"
        #message = f"A new request"
        from_email = 'mikh.kostarev@yandex.ru'
        #recipient_list = ['hangdi1990@gmail.com']
        recipient_list = {instance.email}
        send_mail(sudject, message, from_email, recipient_list)

