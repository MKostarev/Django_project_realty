from django.views.generic import ListView
from managers.models import Managers

class IndexManagersView(ListView):
    model = Managers
    template_name = 'index_managers.html'
    context_object_name = 'managers'



