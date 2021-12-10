from django.db import models

class State(models.Model):
    name = models.CharField(max_length=30)
    country = models.ForeignKey("Country", related_name='states', on_delete=models.CASCADE)