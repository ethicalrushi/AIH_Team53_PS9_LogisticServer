from django.urls import include, path
from . import views

urlpatterns = [
    path('getShipmentAgency/', views.getShipmentAgency),
    path('getShipmentAgency/<int:pk>/', views.ShipmentAgencyDetailView.as_view()),  
    path('dummyAPI/', views.dummyAPI),
    path('dummy/', views.dummy),
    path('getShipmentId/', views.getShipmentId),
    path('getShipmentOrdersShipper/', views.getShipmentOrdersShipper),
    path('setShipFrom/', views.setShipFrom),
    path('setShipTo/', views.setShipTo),
    path('addCustomerOrder/', views.addCustomerOrder),
    path('setShipmentAgency/', views.setShipmentAgency),

    path('scanQRCode/<str:shipmentId>/', views.scanQRCode),
    
    path('getPendingOrdersReceiver/', views.getPendingOrdersReceiver),
    path('getOrderDetails/<str:shipmentId>/', views.getOrderDetails),
    path('blockPayment/', views.blockReceiverPayment),
    path('getScores/', views.getScores),
    path('finalPayment/', views.finalPayment),
    path('getRemainingCost/<str:shipmentId>/', views.getTotalCost),

    #############ShipmentAgencyAPI###############
    path('setCarrier/', views.setCarrier),
    path('setCarrierInformation/', views.setCarrierInformation),
    path('setTrackingInformation/', views.setTrackingInformation),
    path('getTrackingInformation/<str:shipmentId>/', views.getTrackingInformation),
    path('html_bol/<str:shipmentId>/',views.html_bol,name='html_bol')
    
]