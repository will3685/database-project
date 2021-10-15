from django.shortcuts import render, get_object_or_404
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from api.models import *
from api.serializers import *
from rest_framework import status

class HairList(APIView):
  def get(self, request):
      hairs = Hair.objects.all()
      data = HairSerializer(hairs, many=True).data
      return Response(data)

  def post(self, request):
        # haircategory_id =request.data[haircategory_id]
        # haircategory = get_object_or_404(HairCategory, id=haircategory_id)
        # price = request.data["price"]
        # description = request.data["description"]
        # hair = Hair(haircategory=haircategory,price=price,descriptio=description)
        # hair.save()
        # serializer = HairSerializer(hair).data

      serializer = HairSerializer(data=request.data)
      serializer.is_valid(raise_exception=True)
      serializer.save()
      return Response(serializer.data)


