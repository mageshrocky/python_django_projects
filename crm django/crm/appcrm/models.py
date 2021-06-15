from datetime import datetime
from uuid import uuid4

from django.db import models


# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=12)
    product_name = models.CharField(max_length=50)
    order_date = models.CharField(max_length=30)
    delivery_date = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Shop(models.Model):
    product = models.CharField(max_length=50)

    def __str__(self):
        return self.product