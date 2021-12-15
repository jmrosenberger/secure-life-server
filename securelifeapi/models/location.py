from django.db import models

class Location(models.Model):
    city = models.CharField(max_length=100)
    park = models.CharField(max_length=100)
    @property
    def is_visited(self):
        return len(self.places_visited.all()) > 0