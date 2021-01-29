from rest_framework import serializers
from .models import ShipmentAgency
from rest_framework import status
from rest_framework.response import Response

class ShipmentAgencySerializer(serializers.ModelSerializer):
    class Meta:
        model = ShipmentAgency
        fields = ['name', 'cost', 'representative']