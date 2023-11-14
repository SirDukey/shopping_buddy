from django.db import models
from datetime import datetime


class Product(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100, default=None, null=True)
    store = models.CharField(max_length=100, default=None, null=True)
    category = models.CharField(max_length=100, default=None, null=True)
    gluten_free = models.BooleanField(default=False)
    price = models.FloatField(default=0)
    date = models.DateField(default=datetime.today(), null=False)
