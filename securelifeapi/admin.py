from django.contrib import admin
from securelifeapi.models import Adventure, City, Country, Growth, Human, Image, JournalEntry, Location, Park, PlacesVisited, State, Tag
from securelifeapi.models.growth_image import GrowthImage

# Register your models here.

admin.site.register(Adventure)
admin.site.register(City)
admin.site.register(Country)
admin.site.register(Growth)
admin.site.register(Human)
admin.site.register(Image)
admin.site.register(JournalEntry)
admin.site.register(Location)
admin.site.register(Park)
admin.site.register(PlacesVisited)
admin.site.register(State)
admin.site.register(Tag)
admin.site.register(GrowthImage)
