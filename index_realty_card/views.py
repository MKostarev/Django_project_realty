from django.shortcuts import render
from django.views.generic import CreateView

from realty.models import Realty
from request.forms import RerustForm
from request.models import Rerust

def realty_detail_view(request, id):
    realty_card = Realty.objects.get(id=id)
    cat_id = realty_card.cat.id
    if request.method == 'POST':
        form = RerustForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = RerustForm()
    similar_object = Realty.objects.filter(cat=cat_id)
    return render(request, 'realty_card.html', {'realty_card': realty_card, 'form': form, 'similar_object':similar_object})

