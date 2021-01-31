from django.shortcuts import render
from .models import ShipmentAgency, ShipmentOrder
from user.models import User
from rest_framework import viewsets, permissions,generics
from .serializers import ShipmentAgencySerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 
from rest_framework import status
import random
import string

class ShipmentAgencyListView(generics.ListCreateAPIView):

    queryset = ShipmentAgency.objects.all()
    serializer_class = ShipmentAgencySerializer

class ShipmentAgencyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShipmentAgency.objects.all()
    serializer_class = ShipmentAgencySerializer

"""
Sample Api
1) the decorator @api_view can have get/post argument as required
2) you can get all the input data from request.data['key']
3) process the inputs to get required output
4) form a dictionary with keys for formatted output
5) return the dictionary as response object
"""

@api_view(['post'])
def dummyAPI(request):

    #get any input data like this
    shipmentId = request.data["shipmentData"]

    #do some processing with web3.py over here and get the output tuple

    #if everythong is ok that is request was correct then form output
    responseDictionary = {}
    responseDictionary["shipmentId"] = shipmentId
    #add as many keys as required
    return Response(responseDictionary, status=status.HTTP_200_OK)

    """
    else if some error or incorect id or something bad
    return Response({}, status=status.HTTP_400_BAD_REQUEST)

    you can use other status codes too as required

    """

@api_view(['post'])
def dummy(request):
    print(request.data)
    dic = {"shipmentId":request.data["shipmentId"]}
    return Response(dic, status=status.HTTP_200_OK)

@api_view(['get'])
def getShipmentId(request):
    while True:
        randomString = ''.join(random.choices(string.ascii_uppercase +
                                string.digits, k = 6))
        users = User.objects.all()
        user = users[0]
        try:
            shipmentOrder = ShipmentOrder.objects.get(shipmentId=randomString)
        except:
            shipmentOrder = ShipmentOrder(shipmentId=randomString, shipper=user)
            shipmentOrder.save()
            return Response({"shipmentId":randomString}, status=status.HTTP_200_OK)
        else:
            pass

@api_view(['get'])
def getShipmentOrdersShipper(request):

    user = User.objects.all()[0] #get from token
    shipmentOrders = ShipmentOrder.objects.filter(shipper=user)

    shipmentIds = [shipmentOrder.shipmentId for shipmentOrder in shipmentOrders]
    #query this dic from contract for given shipmentIds
    dic = {"shipFrom":"aBC",
            "shipTo":"xyz",
            "shipmentId":"1aenjd",
            "shipmentAgency":"RMD LTD.",
            "approved":False}

    dataList = [dic, dic, dic, dic]

    return Response(dataList, status=status.HTTP_200_OK)
