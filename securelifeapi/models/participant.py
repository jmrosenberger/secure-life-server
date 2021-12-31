from django.db import models

class Participant(models.Model):
    # creator = models.ForeignKey('Creator', on_delete=models.CASCADE)
    human = models.ForeignKey("Human", on_delete=models.CASCADE)
    adventure = models.ForeignKey("Adventure", on_delete=models.CASCADE)
    