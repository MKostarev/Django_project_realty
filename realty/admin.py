from django.contrib import admin

from django.contrib import admin

# Register your models here.
from django.contrib import admin
from realty.models import Realty, Category_realty, Gallery

class GalleryInline(admin.TabularInline):
    fk_name = 'realty'
    model = Gallery

class RealtyAdminView(admin.ModelAdmin):
    list_display = ('name', 'adres', 'info', 'cat', 'id', 'price', 'area', 'managers')
    search_fields = ('name', 'adres')
    list_display_links = ('name', 'adres')
    inlines = [GalleryInline, ]

#class CatAdminView(admin.ModelAdmin):
#    list_display = ('cat', 'id')


admin.site.register(Realty, RealtyAdminView)
admin.site.register(Category_realty)
admin.site.register(Gallery)