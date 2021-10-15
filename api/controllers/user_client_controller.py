from django.shortcuts import render, get_object_or_404
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from api.models import *
from api.serializers import *

class UserClientList(APIView):
  def get(self, request):
      userclient = UserClient.objects.all()
      data = UserClientSerializer(userclient, many=True).data
      return Response(data)

  def post(self, request):
      # user_name = request.data["user_name"]
      # user_email = request.data["user_email"]
      # phone_number = request.data["phone_number"]
      # userclient = UserClient(user_name=user_name, user_email=user_email, 
      # phone_number=phone_number)
      # userclient.save()
      # serializer = UserClientSerializer(userclient).data

      serializer = UserClientSerializer(data=request.data)
      serializer.is_valid(raise_exception=True)
      serializer.save()
      return Response(serializer.data)

# class UserClientDetail(APIView):
#   def get(self,request, id):
#     userclient = get_object_or_404(UserClient, id=id)
#     serializer = UserClientSerializer(userclient).data
#     return Response(serializer)



     

