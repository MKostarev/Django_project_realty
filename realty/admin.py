from django.contrib import admin

from django.contrib import admin

# Register your models here.
from django.contrib import admin
from realty.models import Realty, Category_realty


class RealtyAdminView(admin.ModelAdmin):
    list_display = ('name', 'adres', 'info', 'cat', 'id', 'img')
    search_fields = ('name', 'adres')
    list_display_links = ('name', 'adres')


admin.site.register(Realty, RealtyAdminView)
admin.site.register(Category_realty)