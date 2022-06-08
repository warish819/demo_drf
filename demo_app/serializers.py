from dataclasses import field, fields
from unicodedata import name
from rest_framework import serializers
from demo_app.models import Entry
from django.contrib.auth.models import User, Group


# class CustomSerializer(serializers.Serializer):
#     city = serializers.CharField(max_length=30)

#     class Meta:


class DemoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Entry
        fields= '__all__'

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= User
        fields= '__all__'
        include = 'url'


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Group
        fields = '__all__'
        include = 'url'
                              
           