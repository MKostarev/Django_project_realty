from django.shortcuts import render
#from django.views.generic import CreateView

from managers.models import Managers
from realty.models import Realty
from request.forms import RerustForm



# Create your views here.

def manager_detail_view(request, id):
    manager_card = Managers.objects.get(id=id)
    realty = Realty.objects.all()
    form = RerustForm()
    return render(request, 'index_manager_card.html', {'manager_card': manager_card, 'form': form, 'realty': realty})
