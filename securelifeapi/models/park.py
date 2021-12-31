from django.db import models

class Park(models.Model):
    creator = models.ForeignKey('Creator', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    state = models.CharField(max_length=50)