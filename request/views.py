from django.shortcuts import render
from django.views.generic import CreateView
from request.models import Rerust


# Create your views here.

class FormView (CreateView):
    template_name = 'request/request.html'
    model = Rerust
    fields = ('name', 'email', 'question')
    success_url = '/'
