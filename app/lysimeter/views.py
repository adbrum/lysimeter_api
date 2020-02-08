from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User, Group
from .models import Reading
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, GroupSerializer, ReadingSerializer
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

class ReadingViewSet(viewsets.ModelViewSet):
    queryset = Reading.objects.all()
    serializer_class = ReadingSerializer

    def get(self, request):
        print('Classed base view get')
        try:
            reading = Reading.objects.get(pk=pk)
        except Reading.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = ReadingSerializer(instance=reading, context={'request': request})
            return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        print(request.data) # Delete
        is_many = isinstance(request.data, list)
        if not is_many:
            return super(ReadingViewSet, self).create(request, *args, **kwargs)
        else:
            serializer = self.get_serializer(data=request.data, many=True)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            print(serializer.data) # Delete
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


def app(request):
    return HttpResponse("""
        <h1>Under construction</h1>
        <p>This is going to be the front end app.<p>
        """)
    
@api_view(['GET', 'POST'])
def reading_list(request):
    """
    List all code readings, or create a new reading.
    """
    if request.method == 'GET':
        readings = Reading.objects.all()
        serializer = ReadingSerializer(readings, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ReadingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['GET', 'PUT', 'DELETE'])
def reading_detail(request, pk):
    """
    Retrieve, update or delete a code reading.
    """
    try:
        reading = Reading.objects.get(pk=pk)
    except Reading.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ReadingSerializer(reading)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ReadingSerializer(reading, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        reading.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)