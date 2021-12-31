from django.db import models

class EventImage(models.Model):
    # creator = models.ForeignKey('Creator', on_delete=models.CASCADE)
    event = models.ForeignKey('Event', on_delete=models.CASCADE, related_name='event_images')
    action_pic = models.ImageField(
        upload_to='eventimages', height_field=None,
        width_field=None, max_length=None, null=True)
    