from rest_framework import serializers
from user.models import *
from rest_framework import status
from rest_framework.response import Response

class UserSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField(source='get_token')
    def get_token(self, obj):
        tokenObj = Token.objects.get(user=obj)
        return tokenObj.key

    def create(self, valid_data):
        user = User(name = valid_data['name'],
                    companyName=valid_data['companyName'],
                    contact = valid_data['contact'],
                    address = valid_data['address'],
                    city = valid_data['city'],
                    state = valid_data['state'],
                    zipcode = valid_data['zipcode'],
                    role = valid_data['role'],
                    publicAddress = valid_data['publicAddress'],
                    )

        user.username = user.contact
        user.set_password(valid_data['password'])
        user.save()
        return user


    class Meta:
        model = User
        fields = ['name', 'password', 'companyName','contact','address','city','state','zipcode','role', 'token', 'publicAddress']