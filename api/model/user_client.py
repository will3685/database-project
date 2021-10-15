from django.db import models
from django.db.models.fields import CharField, EmailField

class UserClient(models.Model):
  user_name = models.CharField(max_length=20)
  user_email = models.EmailField(max_length=254)
  phone_number = models.CharField(max_length=15)
  class Meta:
    db_table = 'User_Client'