from django.shortcuts import render
from rest_framework import viewsets

from api.serializers import RealtySerializers
from realty.models import Realty


# Create your views here.

class RealtyApiView(viewsets.ModelViewSet):
    queryset = Realty.objects.all()
    serializer_class = RealtySerializers
