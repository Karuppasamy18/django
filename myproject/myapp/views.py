from django.http import response
from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework import viewsets


class Basetabledata(viewsets.ModelViewSet):
    queryset = Basetable.objects.all()
    serializer_class = BasetableSerializers

class Propertiesdata(viewsets.ModelViewSet):
    queryset=Properties.objects.all()
    serializer_class=PropertiesSerializers


class Dimensionsdata(viewsets.ModelViewSet):
    queryset= Dimensions.objects.all()
    serializer_class=DimensionsSerializers


class Imagesdata(viewsets.ModelViewSet):
    queryset=Images.objects.all()
    serializer_class=ImagesSerializers

class Productdata(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializers


