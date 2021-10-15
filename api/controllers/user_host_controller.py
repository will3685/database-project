from django.shortcuts import render, get_object_or_404
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from api.models import *
from api.serializers import *

class UserHostList(APIView):
  def get(self, request):
      userhost = UserHost.objects.all()
      data = UserHostSerializer(userhost, many=True).data
      return Response(data)

  def post(self, request):
      # user_name = request.data["user_name"]
      # user_email = request.data["user_email"]
      # phone_number = request.data["phone_number"]
      # userclient = UserClient(user_name=user_name, user_email=user_email, 
      # phone_number=phone_number)
      # userclient.save()
      # serializer = UserClientSerializer(userclient).data

      serializer = UserHostSerializer(data=request.data)
      serializer.is_valid(raise_exception=True)
      serializer.save()
      return Response(serializer.data)

class UserHostDetail(APIView):
  def get(self,request, id):
    userhost = get_object_or_404(UserHost, id=id)
    serializer = UserHostSerializer(userhost).data
    return Response(serializer)

class UniqueCategoryBookDetail(APIView):
  def get(self,request, id):
    userhost = get_object_or_404(UserHost, id=id)
    serializer = UniqueCategoryBookSerializer(userhost).data
    return Response(serializer)



     

