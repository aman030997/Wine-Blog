# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models




class Table1(models.Model):
    id = models.CharField(primary_key=True, max_length=3)
    country = models.CharField(max_length=12, blank=True, null=True)
    description = models.CharField(max_length=427, blank=True, null=True)
    designation = models.CharField(max_length=61, blank=True, null=True)
    points = models.CharField(max_length=6, blank=True, null=True)
    price = models.CharField(max_length=5, blank=True, null=True)
    province = models.CharField(max_length=18, blank=True, null=True)
    region_1 = models.CharField(max_length=28, blank=True, null=True)
    region_2 = models.CharField(max_length=23, blank=True, null=True)
    variety = models.CharField(max_length=33, blank=True, null=True)
    winery = models.CharField(max_length=29, blank=True, null=True)

    class Meta:
        db_table = 'table 1'
