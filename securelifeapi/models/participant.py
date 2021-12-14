from django.db import models

class Participant(models.Model):
    human = models.ForeignKey("Human", on_delete=models.CASCADE)
    adventure = models.ForeignKey("Adventure", on_delete=models.CASCADE)
    