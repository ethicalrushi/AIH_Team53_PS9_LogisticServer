from django.shortcuts import render
from .models import User
from rest_framework import viewsets, permissions,generics
from .serializers import UserSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 
from transaction.views import web3Setup, getAccountBalance

class UserListView(generics.ListCreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer



class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['get'])
def getUserDetails(request):
    user = request.user
    print(user)
    return Response({"name":user.name, "role":user.role})

