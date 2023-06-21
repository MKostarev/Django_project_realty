from django.db.models import Q

from django.views.generic import ListView
from realty.models import Realty


class IndexRealtySearchResult(ListView):
    model = Realty
    template_name = 'realty_search.html'
    context_object_name = 'all_realty'

    def get_queryset(self):
       query = self.request.GET.get('q')

       if query:
           queryset = Realty.objects.filter(Q(info__icontains=query) | Q(adres__icontains=query) | Q(name__icontains=query))
       else:
           queryset = Realty.objects.all()

       min = self.request.GET.get('min')
       max = self.request.GET.get('max')

       if min:
           queryset = queryset.filter(price__gte=min)

       if max:
           queryset = queryset.filter(price__lte=max)

       return queryset


