from django.db import models

class Realty (models.Model):
    name = models.CharField(max_length=50)
    adres = models.CharField(max_length=300)
    info = models.TextField()
    img = models.ImageField(upload_to='img')
    cat = models.ForeignKey('Category_realty', on_delete=models.PROTECT)
    price = models.IntegerField(blank=True, null=True)
    area = models.IntegerField(blank=True, null=True)



class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery')
    realty = models.ForeignKey(Realty, on_delete=models.PROTECT, null=True, blank=True, related_name='gallery')



class Category_realty(models.Model):
    cat = models.CharField(max_length=50)

    def __str__(self):
        return self.cat
