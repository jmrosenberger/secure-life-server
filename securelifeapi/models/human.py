from django.db import models
# from django.contrib.auth.models import User


class Human(models.Model):
    creator = models.ForeignKey('Creator', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    birthday = models.DateField(auto_now=False, auto_now_add=False)
    age = models.IntegerField()
    # user = models.ForeignKey(User, related_name='humans', on_delete=models.CASCADE)
