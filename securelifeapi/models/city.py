from django.db import models

class City(models.Model):
    name = models.CharField(max_length=50)
    state = models.ForeignKey("State", related_name='cities', on_delete=models.CASCADE)