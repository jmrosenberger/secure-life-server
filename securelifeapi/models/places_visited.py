from django.db import models

class PlacesVisited(models.Model):
    creator = models.ForeignKey('Creator', on_delete=models.CASCADE)
    adventure = models.ForeignKey('Adventure', related_name='places_visited', on_delete=models.CASCADE)
    location = models.ForeignKey('Location', related_name='places_visited', on_delete=models.CASCADE)