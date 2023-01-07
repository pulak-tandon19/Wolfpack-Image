from rest_framework.serializers import ModelSerializer
from rest_framework import serializers 
from .models import *

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageEdit
        fields = ['img']

class ImageEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageEdit
        fields = ['img1', 'img2', 'img3', 'img4']