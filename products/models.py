from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price_purchase = models.DecimalField(max_digits=10, decimal_places=0)
    price_sale = models.DecimalField(max_digits=10, decimal_places=0)
    quantity = models.IntegerField()
    quantity_sold = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    image = models.URLField(max_length=500, blank=True, null=True)
