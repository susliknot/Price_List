from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    label = models.IntegerField(null=True)

    def __str__(self):
        return self.name


class Price(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField()
    date = models.DateField()

    def __str__(self):
        return self.product.name