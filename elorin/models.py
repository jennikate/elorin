from django.db import models

# Create your models here.

# ----- LOCATIONS
class Continent(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

class Country(models.Model):
    continent = models.ForeignKey(Continent, related_name='continent', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=2000, null=True, blank=True)
    def __str__(self):
        return f'{self.name}'

class Region(models.Model):
    country = models.ForeignKey(Country, related_name='country', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=2000, null=True, blank=True)
    def __str__(self):
        return f'{self.name}'

class Place(models.Model):
    region = models.ForeignKey(Region, related_name='region', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=2000, null=True, blank=True)
    def __str__(self):
        return f'{self.name}'


# ----- NATIONS
class Race(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=2000, null=True, blank=True)
    def __str__(self):
        return f'{self.name}'

class SubRace(models.Model):
    race = models.ForeignKey(Race, related_name='race', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=2000, null=True, blank=True)
    def __str__(self):
        return f'{self.name}'

class Tribe(models.Model):
    subrace = models.ForeignKey(SubRace, related_name='subrace', on_delete=models.CASCADE)
    country = models.ForeignKey(Country, related_name='tribe_country', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=2000, null=True, blank=True)
    def __str__(self):
        return f'{self.name}'
