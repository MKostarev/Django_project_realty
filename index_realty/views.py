from msilib.schema import ListView
from realty.models import Realty

from django.shortcuts import render
from django.views.generic import ListView

from realty.models import Realty, Category_realty
from managers.models import Managers


#def realtyy_view (request, category=None):
#
#    if category == None:
#        all_realty = Realty.objects.all()
#        context = {'all_realty': all_realty}
#
#    else:
#        all_realty = Realty.objects.filter(cat=category)
#        context = {'all_realty': all_realty}
#
#    cat = Category_realty.objects.all()
#    context['cat'] = cat
#
#    return render(request, 'home.html', context)


class IndexrealtyView(ListView):
    template_name = 'index_realty.html'
    model = Realty
    context_object_name = 'all_realty'
