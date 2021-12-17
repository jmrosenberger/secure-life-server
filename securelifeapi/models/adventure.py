from django.db import models

class Adventure(models.Model):
    title = models.CharField(max_length=50)
    participants = models.ManyToManyField("Human", through="Participant")
    date = models.DateField(auto_now=False, auto_now_add=False)
    description = models.CharField(max_length=500)
    