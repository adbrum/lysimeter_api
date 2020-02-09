from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User, Group
from .models import *
from rest_framework import viewsets, permissions
from .serializers import *
from rest_framework.decorators import api_view, permission_classes

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class DeviceParamsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows readings to be viewed or edited.
    """
    queryset = DeviceParams.objects.all()
    serializer_class = DeviceParamsSerializer


def app(request):
    return HttpResponse("""
        <h1>Under construction</h1>
        <p>This is going to be the front end app.<p>
        """)
    