from django.shortcuts import render
from django.views.generic import CreateView

from realty.models import Realty
from request.forms import RerustForm
from request.models import Rerust


# Create your views here.

def realty_detail_view(request, id):
    realty_card = Realty.objects.get(id=id)
    #form = RerustForm()
    if request.method == 'POST':
        form = RerustForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = RerustForm()
    #similar_realty = Realty.objects.filter(cat=)
    return render(request, 'realty_card.html', {'realty_card': realty_card, 'form': form})

#class IndexBaseView (CreateView):
#    template_name = 'realty_card.html'
#    model = Rerust
#    fields = ('name', 'email', 'question')
#    success_url = '/index_home'


#class Realty_detail_view (ListView):
#    template_name = 'index.html'
#    realty_card = Realty.objects.get(id=id)
#    model = Realty
#    context_object_name = 'all_realty'

