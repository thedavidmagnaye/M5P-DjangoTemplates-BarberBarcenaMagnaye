from django.db import models

# Create your models here.
class Supplier(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    
    def getName(self):
        return self.name
    
    def __str__(self):
        return f"{self.name} - {self.city}, {self.country} created at: {self.created_at}"


class WaterBottle(models.Model):
    sku = models.CharField(max_length=50, unique=True)
    brand = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=50)
    mouth_size = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='water_bottles')
    current_quantity = models.IntegerField(default=0)
    
    def __str__(self):
        return (f"{self.sku}: {self.brand}, {self.mouth_size}, {self.size}, "
                f"{self.color}, supplied by {self.supplier.getName()}, "
                f"{self.cost} : {self.current_quantity}")