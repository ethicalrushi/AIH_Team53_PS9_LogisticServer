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

# class ShipmentAgencyListView(generics.ListCreateAPIView):

#     queryset = ShipmentAgency.objects.all()
#     serializer_class = ShipmentAgencySerializer

@api_view(['get'])
def getShipmentAgency(request):
    shipmentAgencyList = ShipmentAgency.objects.all()
    dataList = []
    for shipmentAgency in shipmentAgencyList:
        dic = {}
        dic['name'] = shipmentAgency.name
        dic['cost'] = shipmentAgency.cost
        dic['pk'] = shipmentAgency.pk
        dataList.append(dic)

    response = {"data":dataList}
    return Response(response)

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
    address = web3.toChecksumAddress(constants.contractAddress)
    contract = web3.eth.contract(address=address, abi=abi)
    return contract, web3

@api_view(['get'])
def getShipmentId(request):
    while True:
        randomString = ''.join(random.choices(string.ascii_uppercase +
                                string.digits, k = 6))
        randomString+= ''.join(random.choices(
                                string.digits, k = 8))
        user = request.user
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
    print(shipmentId)
    bolNo = "".join(i for i in shipmentId if i in {str(j) for j in range(10)})
    
    name = request.user.name
    # contact = request.data["contact"]
    address = request.user.address
    city = request.user.city
    state = request.user.state
    country = request.user.country
    zipcode = request.user.zipcode
        
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
    
    contact = request.data["contact"]
    user = User.objects.get(contact=contact)
    name = user.name
    address = user.address
    city = user.city
    state = user.state
    country = user.country
    zipcode = user.zipcode
    
    bolNo = "".join(i for i in shipmentId if i in {str(j) for j in range(10)})

    shipmentOrder = ShipmentOrder.objects.get(shipmentId=shipmentId)
    shipmentOrder.receiver = user
    shipmentOrder.save()

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
    # document = request.data["document"]

    contract, web3 = web3Setup()

    tx_hash = contract.functions.setOrderInformation(shipmentId, customerOrderNumber, numberOfPackages, weight, 0, remarks, int(cost) ).transact()
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
    print(request.data)
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

    user = request.user 
    shipmentOrders = ShipmentOrder.objects.filter(shipper=user)

    # shipmentIds = ["r23A",]
    shipmentIds = [shipmentOrder.shipmentId for shipmentOrder in shipmentOrders]

    dataList = []
    for shipmentId in shipmentIds:
        data = contract.functions.getOrderSnapshot(shipmentId).call()
        dic = {}
        dic["shipFrom"]=data[0]
        dic["shipToName"] = data[1]
        dic["shipmentId"] = shipmentId
        dic["shipmentAgency"] = "RMT LTD" #get from db(shipmentorder) later
        dic["approved"] = data[2]
        dic["shipToCity"] = "city"
        dataList.append(dic)

    print(dataList)
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

"""
{
    "shipmentId":"r23A",
    "longitude":"23.311",
    "latitude":"31.421",
    "approved":"1",
    "remarks":""
}
"""
#can give an option to add documents and attach ipfs links
@api_view(['post'])
def setTrackingInformation(request):
    shipmentId = request.data["shipmentId"]
    date = datetime.datetime.now()
    time = date.strftime("%H:%M:%S")
    date = date.strftime("%d %B %Y")
    longitude = request.data["longitude"]
    latitude = request.data["latitude"]
    user = User.objects.all()[0] #get from auth
    reporterCompanyName = user.companyName
    approved = bool(request.data["approved"])
    remarks = request.data["remarks"]

    contract, web3 = web3Setup()

    tx_hash = contract.functions.setTrackingData(shipmentId, date, time, longitude, latitude, reporterCompanyName, approved, remarks).transact()
    web3.eth.waitForTransactionReceipt(tx_hash)
    return Response({"shipmentId":shipmentId})

@api_view(['get'])
def getTrackingInformation(request, shipmentId):
    contract, web3 = web3Setup()

    data = contract.functions.getTrackingData(shipmentId).call()

    dataList = []
    for d in data:
        dic = {}
        dic["date"] = d[0]
        dic["time"] = d[1]
        dic["longitude"] = d[2]
        dic["latitude"] = d[3]
        dic["companyName"] = d[4]
        dic["approved"] = d[5]
        dic["remark"] = d[6]
        dataList.append(dic)
    print(dataList)
    return Response(dataList)

@api_view(['get'])
def scanQRCode(request, shipmentId):
    contract, web3 = web3Setup()

    user = request.user

    shipmentOrder = ShipmentOrder.objects.get(shipmentId=shipmentId)

    d = contract.functions.getScanDetails(shipmentId).call()

    #get agency predictions here

    dic = {}
    dic["weight"] = d[0]
    dic["packages"] = d[1]
    dic["shipFromName"] = d[2]
    dic["shipToName"] = d[3]
    dic["shipToCity"] = d[4]
    dic["shipmentId"] = shipmentId
    dic["suggestions"] = ""
    dic['receiver'] = False

    if(shipmentOrder.receiver==user):
        dic['receiver'] = True

    return Response(dic)

def getAccountBalance(web3, address):
    balance = web3.eth.getBalance(address)
    balance = web3.fromWei(balance, "ether")
    return balance

def paymentFunction(web3, private_key, price, account_1, flag, nonce):
    account_2 = web3.eth.accounts[0] #server
    if flag:
        account_2 = account_1
    
    tx = {
        'nonce': nonce,
        'to': account_2,
        'value': web3.toWei(price, "ether"),
        'gas': 2000000,
        'gasPrice': web3.toWei('50', 'gwei'),
    }

    signed_tx = web3.eth.account.signTransaction(tx, private_key)
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    web3.eth.waitForTransactionReceipt(tx_hash)

@api_view(['post'])
def blockReceiverPayment(request):
    contract, web3 = web3Setup()

    shipmentId =request.data["shipmentId"]

    d = contract.functions.getScanDetails(shipmentId).call()

    totalCost = d[5]

    #can get from token
    user = User.objects.get(contact='8329766456')
    userCredit = user.creditScore
    #sender account
    account_1 = user.publicAddress
    userWalletBalance = getAccountBalance(web3, account_1)

    print(totalCost, userWalletBalance/2, userCredit, userWalletBalance+userCredit)
    if(totalCost<userWalletBalance/2+userCredit+2 and userCredit>1):
        price = min(totalCost, max(userWalletBalance/2-2, 0))
        creditUsed = totalCost-price
        print(totalCost, price, creditUsed)
        user.creditScore = userCredit-creditUsed
        user.save()
        print("saving credit", user.creditScore)

        #sender key
        #can get from request
        private_key = '2c59762c4ce23a0c7c304b8ed980db3bba1cbe0b032d14d00f539827b551a307'
        nonce = web3.eth.getTransactionCount(account_1)
        paymentFunction(web3, private_key, price, account_1, False, nonce)

        tx = contract.functions.recievePayment(shipmentId, int(price)).transact()
        web3.eth.waitForTransactionReceipt(tx)
        return Response({"true":True})

    else:
        #Insufficient balance
        print("insufficeien")
        return Response({"true":False}, status=status.HTTP_403_FORBIDDEN)

@api_view(['get'])
def getScores(request):
    user = request.user
    address = request.user.publicAddress
    creditScore = user.creditScore

    web3, contract = web3Setup()
    walletBalance = getAccountBalance(web3, address)
    return Response({'creditScore':creditScore, 'balance':walletBalance})

@api_view(['post'])
def finalPayment(request):
    contract, web3 = web3Setup()
    shipmentId =request.data["shipmentId"]
    private_key = '2c59762c4ce23a0c7c304b8ed980db3bba1cbe0b032d14d00f539827b551a307'

    d = contract.functions.getScanDetails(shipmentId).call()
    totalCost = d[5]

    user = request.user
    account_1  = user.publicAddress
    nonce = web3.eth.getTransactionCount(account_1)

    #pay credit
    paymentFunction(web3, private_key, totalCost, account_1, False, nonce)

    tx = contract.functions.recievePayment(shipmentId, int(totalCost)).transact()
    web3.eth.waitForTransactionReceipt(tx)

    shipmentOrder = ShipmentOrder.objects.get(shipmentId=shipmentId)
    shipperAccount = shipmentOrder.shipper.publicAddress

    data = contract.functions.getOrderSnapshot(shipmentId).call()
    amount = data[3]

    contractAccount = web3.eth.accounts[0] 
    nonce = web3.eth.getTransactionCount(contractAccount)

    #pay to shipper
    paymentFunction(web3, private_key, amount, shipperAccount, True, nonce)

    #set delivered

    return Response({"true":True})



