from django.db import models
# from django.contrib.auth.models import User


class Human(models.Model):
    creator = models.ForeignKey('Creator', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    # user = models.ForeignKey(User, related_name='humans', on_delete=models.CASCADE)
