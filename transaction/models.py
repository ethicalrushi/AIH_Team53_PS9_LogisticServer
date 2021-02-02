from django.db import models
from user.models import User

class ShipmentAgency(models.Model):
    name = models.CharField(max_length=200)
    publicAddress = models.CharField(max_length=200, null=True, blank=True)
    cost = models.IntegerField()
    representative = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class ShipmentOrder(models.Model):
    shipmentId = models.CharField(max_length=6)
    shipper = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    ShipmentAgency = models.ForeignKey(ShipmentAgency, blank=True, null=True, on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name='recievers')
    def __str__(self):
        return self.shipmentId

