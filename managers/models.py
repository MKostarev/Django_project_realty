from django.db import models

#from realty.models import Realty


class Managers(models.Model):
    name = models.CharField(max_length=100)
    telefon = models.CharField(max_length=15)
    email = models.EmailField()
    cat = models.ForeignKey('Category_managers', on_delete=models.PROTECT)
    img = models.ImageField(upload_to='img', blank=True, null=True)
    #realty = models.ForeignKey(Realty, blank=True, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.id} {self.name}"

class Category_managers(models.Model):
    cat = models.CharField(max_length=50)

    def __str__(self):
        return self.cat

