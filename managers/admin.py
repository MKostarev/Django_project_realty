from django.contrib import admin

from django.contrib import admin
from managers.models import Managers, Category_managers


# Register your models here.
class ManagersAdminView(admin.ModelAdmin):
    list_display = ('name', 'telefon')
    search_fields = ('name', 'telefon')


admin.site.register(Managers, ManagersAdminView)
admin.site.register(Category_managers)