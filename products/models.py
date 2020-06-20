from django.db import models


class Product (models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)


class Discount (models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount_num = models.FloatField()

class JamesDick (models.Model):
    Length = models.FloatField(max_length=255)
    Girth = models.FloatField(max_length=255)
    description = models.CharField(max_length=255)