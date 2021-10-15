from django.db import models
from django.db.models.fields import CharField, EmailField

class UserHost(models.Model):
  # bookcategory = models.ForeignKey('BookCategory', related_name='userhost', on_delete=models.CASCADE, null="True")
  host_name = models.CharField(max_length=20)
  host_email = models.EmailField(max_length=254)
  phone_number = models.CharField(max_length=20)
  class Meta:
    db_table = 'User_Host'