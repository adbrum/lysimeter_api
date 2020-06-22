from django.contrib.auth.models import User, Group
from .models import*
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class DeviceParamsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DeviceParams
        fields = ("url", 
        'id', 
        'created_at',
        'lysimeter',
        'battery',
        'ambient_temperature',
        'ambient_humidity',
        'ambient_light01',
        'ambient_light02',
        'soil_temperature01',
        'soil_temperature02',
        'soil_temperature03',
        'soil_humidity01',
        'soil_humidity02',
        'soil_humidity03',
        'lysimeter_weight',
        'sediment_weight',
        'date_time')


        