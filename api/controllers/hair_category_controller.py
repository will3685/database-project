from django.shortcuts import render, get_object_or_404
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from api.models import *
from api.serializers import *

class HairCategoryList(APIView):
  def get(self, request):
      haircategory = HairCategory.objects.all()
      data = HairCategorySerializer(haircategory, many=True).data
      return Response(data)
  def post(self, request):
        # name = request.data["name"]
        # description = request.data["description"]
        # haircategory = HairCategory( name=name, description=description)
        # description.save()
        # serializer = HairCategorySerializer(haircategory).data

      serializer = HairCategorySerializer(data=request.data)
      serializer.is_valid(raise_exception=True)
      serializer.save()
      return Response(serializer.data)

class HairCategoryDetail(APIView):
  def get(self,request, id):
    haircategory = get_object_or_404(HairCategory, id=id)
    serializer = HairCategorySerializer(haircategory).data
    return Response(serializer)

class UniqueCategoryHairDetail(APIView):
  def get(self, request, id):
    haircategory = get_object_or_404(HairCategory, id=id)
    serializer = UniqueCategoryHairSerializer(haircategory).data
    return Response(serializer)

