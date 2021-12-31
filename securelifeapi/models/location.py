from django.db import models

class Location(models.Model):
    creator = models.ForeignKey('Creator', on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    park = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    @property
    def is_visited(self):
        return len(self.places_visited.all()) > 0