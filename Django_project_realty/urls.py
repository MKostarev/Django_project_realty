from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from index_realty.views import IndexrealtyView
from managers.views import ManagersView
from realty.views import realtyy_view, RealtyListView
from request.views import FormView
from index_base.views import index_base_def
#from index_realty.views import index_realty_def

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<int:category>/', realtyy_view),
    path('', realtyy_view),
    path('managers/', ManagersView.as_view()),
    path('request/', FormView.as_view()),
    path('index/', RealtyListView.as_view()),
    #path('index/', ManagersListView.as_view())
    path('index_base/', index_base_def),
    path('index_realty/', IndexrealtyView.as_view())

]

if settings.DEBUG is True:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
