from django.shortcuts import render
#from django.views.generic import CreateView

from managers.models import Managers
from realty.models import Realty
from request.forms import RerustForm



# Create your views here.

def manager_detail_view(request, id):
    manager_card = Managers.objects.get(id=id)
    realty = Realty.objects.all()
    #form = RerustForm()
    if request.method == 'POST':
        form = RerustForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = RerustForm()
    return render(request, 'index_manager_card.html', {'manager_card': manager_card, 'form': form, 'realty': realty})
