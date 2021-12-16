from django.db import models

class Image(models.Model):
    # tag = models.ForeignKey("Tag", related_name='images', on_delete=models.CASCADE)
    adventure = models.ForeignKey('Adventure', on_delete=models.DO_NOTHING, related_name='images')
    action_pic = models.ImageField(
        upload_to='adventureimages', height_field=None,
        width_field=None, max_length=None, null=True)
    # image_url = models.ImageField()
    # date = models.DateField(auto_now=False, auto_now_add=False)