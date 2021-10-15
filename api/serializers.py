from rest_framework import serializers
from .models import *
from .views import *


class UserClientSerializer(serializers.ModelSerializer):
  class Meta:
    model = UserClient
    fields = '__all__'

class UserHostSerializer(serializers.ModelSerializer):
  class Meta:
    model = UserHost
    fields = '__all__' 

class HairCategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = HairCategory
    fields = '__all__'