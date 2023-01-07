from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from PIL import Image
from .serializers import *
from io import BytesIO
from django.core.files import File
# Create your views here.

class EditImage(APIView):
    def get(self, request, *args, **kwargs):
        data = self.request.data

        image = ImageEdit.objects.create(img = data['img'], img1 = data['img'], img2 = data['img'], img3 = data['img'], img4 = data['img'])
        image.save()
       
        serializer = ImageEditSerializer(image)
        return Response(serializer.data)
        