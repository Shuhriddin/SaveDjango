from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .models import Clients
from .serializers import ClientSerializer
class ClientViewset(ModelViewSet):
    queryset = Clients.objects.all()
    serializer_class = ClientSerializer