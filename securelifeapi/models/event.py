from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField(auto_now=False, auto_now_add=False)
    notes = models.CharField(max_length=500)
    