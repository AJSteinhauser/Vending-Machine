from django.db import models
from pyrsistent import l

# Create your models here.


class Drinks(models.Model):
    name = models.CharField(max_length=30, primary_key=True);
    description = models.TextField();
    price = models.DecimalField(default=1.00,max_digits=5,decimal_places=2);
    inStock = models.IntegerField(default=50);
    maxStock = models.IntegerField(default=50);
    imageName = models.CharField(max_length=30, default=None, null=True);

    def __str__(self):
        return self.name
