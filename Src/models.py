# Models for Django framework
from django.db import models

class Product(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField(blank=True,null=True)
    price=models.DecimalField(decimal_places=2,max_digits=1000)
    summary=models.TextField()
class Account(models.Model):
    accountnumber=models.BigIntegerField(max_length=1000)
    