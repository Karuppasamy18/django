from django.db.models import fields
from rest_framework import serializers
from .models import *


class DimensionsSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Dimensions
        fields = '__all__'

class ImagesSerializers(serializers.ModelSerializer):
   
    class Meta:
        model = Images
        fields = '__all__'

class PropertiesSerializers(serializers.ModelSerializer):
    
    
    class Meta:
        model = Properties
        fields= '__all__'

class ProductSerializers(serializers.ModelSerializer):
    
    
    class Meta:
        model = Product
        fields= '__all__'



class BasetableSerializers(serializers.ModelSerializer):

    
    class Meta:
        model = Basetable
        fields ='__all__'
        
    Properties=PropertiesSerializers(read_only=True,many=True)
    Dimensions=DimensionsSerializers(read_only=True,many=True)
    Images=ImagesSerializers(read_only=True,many=True)
    