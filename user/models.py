from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name=models.CharField(max_length=300)
    companyName = models.CharField(max_length = 300, null=True, blank=True)
    contact=models.CharField(max_length=12)
    address=models.TextField()
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    zipcode = models.CharField(max_length=6)
    
    CHOICES = (
        ('SHP', 'Shipper'),
        ('SPM', 'Shipment Company'),
        ('RCV', 'Reciever'),
        ('INT', 'Intermediate'),
    )
    role=models.CharField(max_length=3,choices=CHOICES)
    publicAddress = models.CharField(max_length=300, null=True, blank=True)

    def get_token(self):
        tokenObj = Token.objects.get(user=self)
        return tokenObj.key

    def __str__(self):
        return self.name

#generating tokens
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)