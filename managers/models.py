from django.db import models

class Managers(models.Model):
    name = models.CharField(max_length=100)
    telefon = models.CharField(max_length=15)
    email = models.EmailField()
    cat = models.ForeignKey('Category_managers', on_delete=models.PROTECT)
    img = models.ImageField(upload_to='img', blank=True, null=True)

class Category_managers(models.Model):
    cat = models.CharField(max_length=50)

    def __str__(self):
        return self.cat

