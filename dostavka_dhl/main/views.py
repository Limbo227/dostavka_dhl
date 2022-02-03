from django.db.models import Avg
from django.shortcuts import render
from requests import Response
from rest_framework.viewsets import ModelViewSet

from .serializers import *
from rest_framework import generics



# Create your views here.
class MainCreationView(generics.CreateAPIView):
    serializer_class = MainSerializers


class MainListView(generics.ListAPIView):
    serializer_class = MainListSerializer
    queryset = Dostavka.objects.all()


class ScaleView(generics.CreateAPIView):
    serializer_class = ScaleSerializer
    queryset = Scale.objects.all()


class ScaleWeightView(generics.CreateAPIView):
    serializer_class = ScaleWeightSerializer
    queryset = Scale_weight.objects.all()



