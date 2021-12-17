from django.db import models

class Image(models.Model):
    adventure = models.ForeignKey('Adventure', on_delete=models.CASCADE, related_name='images')
    action_pic = models.ImageField(
        upload_to='adventureimages', height_field=None,
        width_field=None, max_length=None, null=True)