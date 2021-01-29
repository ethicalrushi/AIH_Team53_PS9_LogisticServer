from django.shortcuts import render
from .models import ShipmentAgency
from rest_framework import viewsets, permissions,generics
from .serializers import ShipmentAgencySerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 

class ShipmentAgencyListView(generics.ListCreateAPIView):

    queryset = ShipmentAgency.objects.all()
    serializer_class = ShipmentAgencySerializer



class ShipmentAgencyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShipmentAgency.objects.all()
    serializer_class = ShipmentAgencySerializer