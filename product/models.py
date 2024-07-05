from django.conf import settings
from django.db import models


# Create your models here.

class Origin(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Species(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class RoastLevel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tested(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Processing(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    variant = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    stock = models.PositiveIntegerField()
    origin = models.ForeignKey(Origin, on_delete=models.SET_NULL, blank=True,
                               null=True)
    species = models.ForeignKey(Species, on_delete=models.SET_NULL,
                                blank=True, null=True)
    roast_level = models.ForeignKey(RoastLevel, on_delete=models.SET_NULL,
                                    blank=True, null=True)
    tested = models.ForeignKey(Tested, on_delete=models.SET_NULL,
                               blank=True, null=True)
    processed = models.ForeignKey(Processing, on_delete=models.SET_NULL,
                                  blank=True, null=True)

    def __str__(self):
        return f'{self.name} - {self.price}'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='product_images',
                                on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return f'{self.product}'
