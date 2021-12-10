from django.db import models

class Park(models.Model):
    name = models.CharField(max_length=50)
    state = models.ForeignKey("State", related_name='parks', on_delete=models.CASCADE)