from django.db import models

class Rerust(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    question = models.TextField()
    question2 = models.TextField(blank=True, null=True)
    id_manager = models.IntegerField(blank=True, null=True)
    object_link = models.TextField(blank=True, null=True)


