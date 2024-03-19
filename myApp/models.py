from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_value = models.IntegerField()
    def __str__(self):
        return self.product_name