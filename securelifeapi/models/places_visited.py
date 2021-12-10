from django.db import models

class PlacesVisited(models.Model):
    adventure = models.ForeignKey('Adventure', related_name='places_visited', on_delete=models.CASCADE)
    location = models.ForeignKey('Location', related_name='places_visited', on_delete=models.CASCADE)