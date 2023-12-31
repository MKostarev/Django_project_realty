from django.db import models
from django.urls import reverse

from managers.models import Managers

class Realty (models.Model):
    name = models.CharField(max_length=50)
    adres = models.CharField(max_length=300)
    info = models.TextField()
    img = models.ImageField(upload_to='img')
    cat = models.ForeignKey('Category_realty', on_delete=models.PROTECT)
    price = models.IntegerField(blank=True, null=True)
    area = models.IntegerField(blank=True, null=True)
    managers = models.ForeignKey(Managers, blank=True, null=True, on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse('realty_card', args=[self.id])


class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery')
    realty = models.ForeignKey(Realty, on_delete=models.PROTECT, null=True, blank=True, related_name='gallery')

class Category_realty(models.Model):
    cat = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.cat} {self.id}"

#class Category_managers2(models.Model):
#    catt2 = models.CharField(max_length=50)
#
#    def __str__(self):
#        return self.cat




#class Managers_realty(models.Model):
#    name = models.CharField(max_length=100)
#    telefon = models.CharField(max_length=15)
#    email = models.EmailField()
#    cat = models.ForeignKey('Category_managers', on_delete=models.PROTECT)
#    img = models.ImageField(upload_to='img', blank=True, null=True)