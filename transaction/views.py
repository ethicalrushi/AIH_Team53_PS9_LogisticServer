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
from web3 import Web3
import json
from . import constants
import datetime

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

def web3Setup():
    ganache_url = "http://127.0.0.1:7545"
    web3 = Web3(Web3.HTTPProvider(ganache_url))
    abi = json.loads(constants.abi)
    web3.eth.defaultAccount = web3.eth.accounts[0]
    address = web3.toChecksumAddress('0x074EC44e6f1De63CD908e24240142371380A4572')
    contract = web3.eth.contract(address=address, abi=abi)
    return contract, web3

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

"""
{"shipmentId":"r23A",
"name":"rushi",
"address":"hari om",
"city":"MUM",
"state":"MH",
"zip":"421605"
}
"""
@api_view(['post'])
def setShipFrom(request):
    date = datetime.datetime.now()
    date = date.strftime("%d %B %Y")
    shipmentId = request.data["shipmentId"]
    bolNo = "".join(i for i in shipmentId if i>='0' and i<='9')
    
    name = request.data["name"]
    # contact = request.data["contact"]
    address = request.data["address"]
    city = request.data["city"]
    state = request.data["state"]
    zipcode = request.data["zip"]
        
    contract, web3 = web3Setup()
    userAddress = web3.toChecksumAddress('0xD1e684503F184464252A7759e817a6333B5F68a9')

    tx_hash = contract.functions.setDate(shipmentId,date).transact()
    web3.eth.waitForTransactionReceipt(tx_hash)

    tx_hash = contract.functions.setBOL_No(shipmentId,int(bolNo)).transact()
    web3.eth.waitForTransactionReceipt(tx_hash)

    tx_hash = contract.functions.setShipFrom(shipmentId, name, address, city, state, int(zipcode), int(bolNo), False, 1, userAddress).transact()
    web3.eth.waitForTransactionReceipt(tx_hash)
    return Response({"shipmentId":shipmentId})

"""
{"shipmentId":"r23A",
"name":"gannu",
"address":"disha",
"city":"NGP",
"state":"MH",
"zip":"42421"
}
"""
@api_view(['post'])
def setShipTo(request):
    shipmentId = request.data["shipmentId"]
    name = request.data["name"]
    # contact = request.data["contact"]
    address = request.data["address"]
    city = request.data["city"]
    state = request.data["state"]
    zipcode = request.data["zip"]
    
    bolNo = "".join(i for i in shipmentId if i>='0' and i<='9')

    contract, web3 = web3Setup()
    userAddress = web3.toChecksumAddress('0xD1e684503F184464252A7759e817a6333B5F68a9')

    tx_hash = contract.functions.setShipTo(shipmentId, name, address, city, state, int(zipcode), int(bolNo), False, 1, userAddress).transact()
    web3.eth.waitForTransactionReceipt(tx_hash)
    return Response({"shipmentId":shipmentId})

"""
{"shipmentId":"r23A",
"orderNumber":"121",
"numberOfPackages":"12",
"weight":"2000",
"cost":"200000",
"remarks":"Fragile"
}
"""
@api_view(['post'])
def addCustomerOrder(request):
    shipmentId = request.data["shipmentId"]
    customerOrderNumber = int(request.data["orderNumber"])
    numberOfPackages = int(request.data["numberOfPackages"])
    weight = int(request.data["weight"])
    cost = int(request.data["cost"]) #to be added to contract
    remarks = request.data["remarks"]

    contract, web3 = web3Setup()

    tx_hash = contract.functions.setOrderInformation(shipmentId, customerOrderNumber, numberOfPackages, weight, 0, remarks ).transact()
    web3.eth.waitForTransactionReceipt(tx_hash)
    return Response({"shipmentId":shipmentId})

"""
{
"shipmentId":"r23A",
"shipmentAgencyId":"0"
}
"""
@api_view(['post'])
def setShipmentAgency(request):
    shipmentId = request.data["shipmentId"]
    shipmentAgencyId = int(request.data["shipmentAgencyId"])

    contract, web3 = web3Setup()

    shipmentAgency = ShipmentAgency.objects.get(pk=shipmentAgencyId)
    shipmentAgencyAddress = web3.toChecksumAddress(shipmentAgency.publicAddress)

    tx_hash = contract.functions.setShipmentAgency(shipmentId, shipmentAgencyId, shipmentAgencyAddress).transact()
    web3.eth.waitForTransactionReceipt(tx_hash)
    return Response({"shipmentId":shipmentId})


@api_view(['get'])
def getShipmentOrdersShipper(request):
    contract, web3 = web3Setup()

    user = User.objects.all()[0] #get from token
    shipmentOrders = ShipmentOrder.objects.filter(shipper=user)

    shipmentIds = ["r23A",]
    # shipmentIds = [shipmentOrder.shipmentId for shipmentOrder in shipmentOrders]

    dataList = []
    for shipmentId in shipmentIds:
        data = contract.functions.getOrderSnapshot(shipmentId).call()
        dic = {}
        dic["shipFrom"]=data[0]
        dic["shipTo"] = data[1]
        dic["shipmentId"] = shipmentId
        dic["shipmentAgency"] = "RMT LTD" #get from db(shipmentorder) later
        dic["approved"] = data[2]
        dataList.append(dic)

    return Response(dataList, status=status.HTTP_200_OK)

#######################ShipmentAgencyAPIs#######################

"""
{
    "shipmentId":"r23A",
    "carrierName":"Jai Bhavani",
    "trailerNumber":"213",
    "sealNumber":"3211",
    "SCAD":"23321",
    "proNumber":"21"
}
"""

@api_view(['post'])
def setCarrier(request):
    shipmentId = request.data["shipmentId"]
    carrierName = request.data["carrierName"]
    trailerNumber = int(request.data["trailerNumber"])
    sealNumber = int(request.data["sealNumber"])
    scad = int(request.data["SCAD"])
    proNumber = int(request.data["proNumber"])

    contract, web3 = web3Setup()
    #make shipmentAgencyApproval True here in contract
    tx_hash = contract.functions.setCarrier(shipmentId, carrierName, trailerNumber, sealNumber, scad, proNumber).transact()
    web3.eth.waitForTransactionReceipt(tx_hash)
    return Response({"shipmentId":shipmentId})

"""
{
    "shipmentId":"r23A",
    "handlingUnitQuantity":"231",
    "handlingUnitType":"0",
    "packageQuantity":"12",
    "packageType":"0",
    "weight":"212",
    "HM":"1",
    "description":"hazardous",
    "NMFC":"1ed32",
    "class":"1A"
}
"""

@api_view(['post'])
def setCarrierInformation(request):
    shipmentId = request.data["shipmentId"]
    handlingUnitQuantity = int(request.data["handlingUnitQuantity"])
    handlingUnitType = bool(request.data["handlingUnitType"])
    packageQuantity = int(request.data["packageQuantity"])
    packageType = bool(request.data["packageType"])
    weight = int(request.data["weight"])
    hm = bool(request.data["HM"])
    description = request.data["description"]
    nmfc = request.data["NMFC"]
    pClass = request.data["class"]

    contract, web3 = web3Setup()

    tx_hash = contract.functions.setCarrierInformation(shipmentId, handlingUnitQuantity, handlingUnitType, packageQuantity, packageType, weight, hm, description, nmfc, pClass).transact()
    web3.eth.waitForTransactionReceipt(tx_hash)
    return Response({"shipmentId":shipmentId})




