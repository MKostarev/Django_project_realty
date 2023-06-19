from django.views.generic import ListView
from realty.models import Realty


class IndexrealtyView(ListView):
    template_name = 'index_realty.html'
    model = Realty
    context_object_name = 'all_realty'
