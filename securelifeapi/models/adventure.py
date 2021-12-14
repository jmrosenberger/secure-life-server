from django.db import models

class Adventure(models.Model):
    title = models.CharField(max_length=50)
    human = models.ForeignKey("Human", related_name='adventures', on_delete=models.CASCADE)
    # location = models.ForeignKey("Location", related_name='adventures', on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=False)
    description = models.CharField(max_length=500)
    # image = models.ForeignKey("Image", related_name='adventures', on_delete=models.CASCADE)