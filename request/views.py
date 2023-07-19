from django.views.generic import CreateView
from request.models import Rerust


class FormView(CreateView):
    template_name = 'request/request.html'
    model = Rerust
    fields = ('name', 'email', 'question')
    success_url = '/'
