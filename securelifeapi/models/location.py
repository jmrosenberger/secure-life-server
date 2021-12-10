from django.db import models

class Location(models.Model):
    city = models.ForeignKey('City', related_name='locations', on_delete=models.CASCADE)
    park = models.ForeignKey('Park', related_name='locations', on_delete=models.CASCADE)