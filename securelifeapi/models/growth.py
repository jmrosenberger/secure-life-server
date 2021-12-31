from django.db import models
# from django.db.models.deletion import CASCADE

class Growth(models.Model):
    creator = models.ForeignKey('Creator', on_delete=models.CASCADE)
    human = models.ForeignKey("Human", related_name='growth', on_delete=models.CASCADE)
    age=models.IntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()
    length = models.IntegerField()
    date = models.DateField(auto_now=False, auto_now_add=False)
    notes = models.CharField(max_length=500)
    