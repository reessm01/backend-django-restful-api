from django.db import models

class Manufacturer(models.Model):
    name = models.CharField(max_length=50)
    website = models.URLField()

    def __str__(self):
        return self.name

class ShoeType(models.Model):
    style = models.CharField(max_length=50)

    def __str__(self):
        return self.style

class ShoeColor(models.Model):
    color_name = models.CharField(max_length=10)

    def __str__(self):
        return self.color_name

class Shoe(models.Model):
    size = models.IntegerField()
    brand_name = models.CharField(max_length=50)
    manufacturer = models.ManyToManyField(Manufacturer)
    color = models.ManyToManyField(ShoeColor)
    material = models.CharField(max_length=50)
    shoe_type = models.ManyToManyField(ShoeType)
    fasten_type = models.CharField(max_length=50)