
from django.views.generic import CreateView

from request.models import Rerust


# Create your views here.


class IndexBaseView (CreateView):
    template_name = 'index_home.html'
    model = Rerust
    fields = ('name', 'email', 'question')
    success_url = '/index_home'