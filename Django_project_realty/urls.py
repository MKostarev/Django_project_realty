from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from index_managers.views import IndexManagersView
from index_realty_search.views import IndexRealtySearchResult
from index_request.views import IndexRequestView
from index_realty.views import IndexrealtyView
from managers.views import ManagersView
from realty.views import realtyy_view, RealtyListView
from request.views import FormView
from index_base.views import IndexBaseView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<int:category>/', realtyy_view),
    path('', IndexBaseView.as_view()),
    path('managers/', ManagersView.as_view()),
    path('request/', FormView.as_view()),
    path('index/', RealtyListView.as_view()),
    path('index_home/', IndexBaseView.as_view()),
    path('index_realty/', IndexrealtyView.as_view()),
    path('index_managers/', IndexManagersView.as_view()),
    path('index_request/', IndexRequestView.as_view()),
    path('realty_search/', IndexRealtySearchResult.as_view(), name='search')



]

if settings.DEBUG is True:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
