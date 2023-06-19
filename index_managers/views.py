from django.views.generic import ListView
from realty.models import Realty

class IndexManagersView(ListView):
    model = Realty
    template_name = 'index_managers.html'
    context_object_name = 'all_realty'