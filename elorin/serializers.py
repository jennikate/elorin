from rest_framework import serializers
from .models import Continent, Country, Region, Place, Race, SubRace, Tribe

class ContinentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Continent
        fields = ('id', 'name', 'description')

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'name', 'continent', 'description')

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('id', 'name', 'country', 'description')

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ('id', 'name', 'region', 'description')

class RaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race
        fields = ('id', 'name', 'description')

class SubRaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubRace
        fields = ('id', 'name', 'race', 'description')

class TribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tribe
        fields = ('id', 'name', 'subrace', 'country', 'description')


# ---- POPULATED SERIALIZERS : to allow single calls to return related data
# There is a better way to do this, I just don't know what it is yet
class PopulatedCountrySerializer(CountrySerializer):
    continent = ContinentSerializer()

class PopulatedRegionSerializer(RegionSerializer):
    country = PopulatedCountrySerializer()

class PopulatedPlaceSerializer(PlaceSerializer):
    region = PopulatedRegionSerializer()
