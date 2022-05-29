from django.db import models

class Color(models.Model):
    hex_color = models.CharField(max_length=8)
    color_name = models.CharField(max_length=200)
    inventory = models.IntegerField(default= 0)

class Flavor(models.Model):
    flavor_name = models.CharField(max_length=200)
    inventory = models.IntegerField(default = 0)

class Batch(models.Model):
    color_id = models.ForeignKey(Color, on_delete=models.PROTECT)
    flavor_id = models.ForeignKey(Flavor, on_delete=models.PROTECT)
    inventory = models.IntegerField(default = 0)

