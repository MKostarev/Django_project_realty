from django.db.models import Q

from django.views.generic import ListView
from realty.models import Realty, Category_realty, Gallery


class IndexRealtySearchResult(ListView):
    model = Realty
    template_name = 'realty_search.html'
    context_object_name = 'all_realty'

    def get_queryset(self):
       query = self.request.GET.get('q')
       min = self.request.GET.get('min')
       max = self.request.GET.get('max')
       min_area = self.request.GET.get('min_area')
       max_area = self.request.GET.get('max_area')
       category = self.request.GET.get('category')


       if query:
           queryset = Realty.objects.filter(Q(info__iregex=query) | Q(adres__iregex=query) | Q(name__iregex=query))
       else:
           queryset = Realty.objects.all()

       if min:
           queryset = queryset.filter(price__gte=min)

       if max:
           queryset = queryset.filter(price__lte=max)

       if min_area:
           queryset = queryset.filter(area__gte=min_area)

       if max_area:
           queryset = queryset.filter(area__lte=max_area)

       if category:
           queryset = queryset.filter(cat=category)

#
       return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = Category_realty.objects.all()
        context['category'] = category
        return context


