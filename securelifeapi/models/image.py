from django.db import models

class Image(models.Model):
    tag = models.ForeignKey("Tag", related_name='images', on_delete=models.CASCADE)
    image_url = models.ImageField()
    date = models.DateField(auto_now=False, auto_now_add=False)