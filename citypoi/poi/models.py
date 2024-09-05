from django.db import models

POI_TYPES = [
    ('landmark', 'Landmark'),
    ('park', 'Park'),
    ('tourist_spot', 'Tourist Spot'),
    ('attraction', 'Attraction'),
    ('historic_site', 'Historic Site'),
    ('cultural_site', 'Cultural Site'),
    ('shopping', 'Shopping'),
    ('cultural_village', 'Cultural Village'),
    ('historic_city', 'Historic City'),
    ('recreation', 'Recreation'),
]

class POI(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    poi_type = models.CharField(max_length=50, choices=POI_TYPES)

    def __str__(self):
        return self.name
