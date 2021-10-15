from rest_framework import serializers
from .models import *
from .views import *
class UserClientSerializer(serializers.ModelSerializer):
  class Meta:
    model = UserClient
    fields = '__all__'