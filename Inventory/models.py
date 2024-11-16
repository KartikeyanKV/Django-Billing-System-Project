from django.db import models

class Products(models.Model):
    product_name = models.CharField(max_length=200,null=True)
    product_id = models.CharField(max_length=100,null=True)
    product_price = models.IntegerField(default=0 )
    product_GST = models.FloatField(default=0)
    picture = models.ImageField(null=True, upload_to='images/')
    
    def __str__(self):
        return self.product_name
    
