from django.db import models
from django.db.models.fields import CharField, IntegerField


class Hair(models.Model):
  haircategory = models.ForeignKey('HairCategory', related_name='hairs', on_delete=models.CASCADE)
  price = models.IntegerField()
  description = models.CharField(max_length=200)
  observation = models.CharField(max_length=400, null="True")
  class Meta:
    db_table = 'Hair'