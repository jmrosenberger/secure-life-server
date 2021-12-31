from django.db import models

class Tag(models.Model):
    creator = models.ForeignKey('Creator', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)