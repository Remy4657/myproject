from django.db import models

# Create your models here.

class Products(models.Model):
    product_name = models.CharField(max_length=200)
    detail = models.CharField(max_length=10000)
    price = models.IntegerField()
    img = models.ImageField(upload_to='images', null=False, default=None)