from rest_framework import serializers

from realty.models import Realty


class RealtySerializers(serializers.ModelSerializer):
    class Meta:
        model = Realty
        fields = ['name', 'adres', 'info', 'img', 'cat', 'price', 'area', 'managers']