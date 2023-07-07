from django.core.mail import send_mail
from django.shortcuts import render
from django.views.generic import CreateView
from request.models import Rerust


class IndexRequestView (CreateView):
    template_name = 'index_request.html'
    model = Rerust
    fields = ('name', 'email', 'question')
    success_url = '/index_home'

#def mailsendview(request):
#    subject = 'test mail'
#    message = 'Hello'
#    from_email = 'Django'
#    recipient_list = ['mikh.kostarev@yandex.ru']
#    send_mail(subject, message, from_email, recipient_list)
#    return render(request, 'index_request.html')