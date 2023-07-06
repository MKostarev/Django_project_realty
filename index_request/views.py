from django.views.generic import CreateView
from request.models import Rerust


class IndexRequestView (CreateView):
    template_name = 'index_request.html'
    model = Rerust
    fields = ('name', 'email', 'question', 'question2')
    success_url = '/index_home'

