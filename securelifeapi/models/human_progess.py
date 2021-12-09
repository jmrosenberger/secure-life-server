from django.db import models
from django.db.models.deletion import CASCADE

class HumanProgress(models.Model):
    human = models.ForeignKey("Human", related_name='humans', on_delete=models.CASCADE)
    height = models.IntegerField()
    weight = models.IntegerField()
    length = models.IntegerField()
    date = models.DateField(auto_now=False, auto_now_add=False)