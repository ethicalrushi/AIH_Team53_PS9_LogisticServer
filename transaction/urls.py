from django.urls import include, path
from . import views

urlpatterns = [
    path('getShipmentAgency/', views.ShipmentAgencyListView.as_view()),
    path('getShipmentAgency/<int:pk>/', views.ShipmentAgencyDetailView.as_view()),  
    path('dummyAPI/', views.dummyAPI),
    path('dummy/', views.dummy),
    path('getShipmentId/', views.getShipmentId),
    path('getShipmentOrdersShipper/', views.getShipmentOrdersShipper),
    
]