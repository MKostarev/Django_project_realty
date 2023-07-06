
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from request.models import Rerust


@receiver(post_save, sender=Rerust)
def send_email_to_manager(sender, instance, created, **kwargs):
    if created:
        sudject = 'New Request'
        #message = f"A new request has been:\n\nName: {instance.name}\nEmail: {instance.email}"
        message = f"A new request"
        from_email = 'Django'
        recipient_list = ['mikh.kostarev@yandex.ru']
        send_mail(sudject, message, from_email, recipient_list)