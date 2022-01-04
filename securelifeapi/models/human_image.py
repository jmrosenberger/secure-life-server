from django.db import models

class HumanImage(models.Model):
    # creator = models.ForeignKey('Creator', on_delete=models.CASCADE)
    human = models.ForeignKey('Human', on_delete=models.CASCADE, related_name='human_images')
    action_pic = models.ImageField(
        upload_to='humanimages', height_field=None,
        width_field=None, max_length=None, null=True)
    