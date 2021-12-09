from django.db import models

class Human(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey("User", related_name='users', on_delete=models.CASCADE)