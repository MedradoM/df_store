from django.db import models

class Products(models.Model):
    product_created_in = models.DateTimeField(auto_now_add=True)
    product_name = models.CharField(max_length=100)
    product_value = models.IntegerField()
    product_image = models.ImageField(upload_to ='uploads/% Y/% m/% d/')
    product_description = models.TextField(max_length=200, default="")
    class Meta:
        ordering = ['product_created_in']
    