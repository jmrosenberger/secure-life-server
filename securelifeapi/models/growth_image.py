from django.db import models

class GrowthImage(models.Model):
    # creator = models.ForeignKey('Creator', on_delete=models.CASCADE)
    growth = models.ForeignKey('Growth', on_delete=models.CASCADE, related_name='growth_images')
    action_pic = models.ImageField(
        upload_to='growthimages', height_field=None,
        width_field=None, max_length=None, null=True)
    