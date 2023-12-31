from django.contrib import admin

from django.contrib import admin
from request.models import Rerust


# Register your models here.
class RequestAdminView(admin.ModelAdmin):
    list_display = ('name', 'email', 'question', 'id_manager', 'object_link')
    search_fields = ('name', 'email')


admin.site.register(Rerust, RequestAdminView)