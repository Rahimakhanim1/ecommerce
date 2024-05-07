from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField()
    discount = models.IntegerField()
    available = models.BooleanField(default=True)
