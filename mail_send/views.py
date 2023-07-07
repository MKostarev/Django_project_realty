from django.core.mail import send_mail
from django.shortcuts import render

# Create your views here.
def mailsendview(request):
    subject = 'test mail'
    message = 'Hello'
    from_email = 'Django'
    recipient_list = ['hangdi1990@gmail.com']
    send_mail(subject, message, from_email, recipient_list)
    return render(request, 'index_request.html')