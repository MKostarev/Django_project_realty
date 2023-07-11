from django.shortcuts import render
from realty.models import Realty


# Create your views here.

def realty_detail_view(request, id):
    realty_card = Realty.objects.get(id=id)



    return render(request, 'realty_card.html', {'realty_card': realty_card})

