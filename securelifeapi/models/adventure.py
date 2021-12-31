from django.db import models

class Adventure(models.Model):
    title = models.CharField(max_length=50)
    creator = models.ForeignKey('Creator', on_delete=models.CASCADE)
    participants = models.ManyToManyField("Human", through="Participant")
    location = models.ForeignKey('Location', related_name='adventures', on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=False)
    description = models.CharField(max_length=500)
    